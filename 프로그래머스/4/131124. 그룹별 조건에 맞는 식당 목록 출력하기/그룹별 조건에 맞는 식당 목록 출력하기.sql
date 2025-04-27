SELECT s.member_name, f.review_text, DATE_FORMAT(f.review_date,"%Y-%m-%d") review_date
FROM rest_review f JOIN member_profile s ON f.member_id = s.member_id
WHERE f.member_id = (
    SELECT member_id
    FROM rest_review
    GROUP BY member_id
    ORDER BY COUNT(*) DESC
    LIMIT 1
)
ORDER BY f.review_date ASC, f.review_text ASC;