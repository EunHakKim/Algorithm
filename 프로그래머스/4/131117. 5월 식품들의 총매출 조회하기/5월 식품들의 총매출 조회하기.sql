-- 코드를 입력하세요
SELECT P.PRODUCT_ID, P.PRODUCT_NAME, P.PRICE * AMOUNT AS TOTAL_SALES
FROM FOOD_PRODUCT P JOIN (
    SELECT PRODUCT_ID, SUM(AMOUNT) AS AMOUNT
    FROM FOOD_ORDER
    WHERE YEAR(PRODUCE_DATE) = 2022 AND MONTH(PRODUCE_DATE) = 5
    GROUP BY PRODUCT_ID
) O ON P.PRODUCT_ID = O.PRODUCT_ID
ORDER BY TOTAL_SALES DESC, P.PRODUCT_ID ASC