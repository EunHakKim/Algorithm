-- 코드를 입력하세요
SELECT DISTINCT CAR_ID, IF (CAR_ID IN (
        SELECT DISTINCT CAR_ID
        FROM CAR_RENTAL_COMPANY_RENTAL_HISTORY
        WHERE START_DATE <= DATE("2022-10-16") AND END_DATE >= DATE("2022-10-16")
    ), "대여중", "대여 가능"
) AS AVAILABILITY
FROM CAR_RENTAL_COMPANY_RENTAL_HISTORY
ORDER BY CAR_ID DESC