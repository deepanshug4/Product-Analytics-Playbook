WITH fee_bucket AS (

SELECT
    CASE
        WHEN delivery_fee < 30 THEN '0-30'
        WHEN delivery_fee < 50 THEN '30-50'
        WHEN delivery_fee < 70 THEN '50-70'
        ELSE '70+'
    END AS fee_bucket,

    COUNT(*) AS sessions,

    SUM(
        CASE
            WHEN completed THEN 1
            ELSE 0
        END
    ) AS completed_orders

FROM sessions

GROUP BY 1

)

SELECT

fee_bucket,

sessions,

completed_orders,

ROUND(
    completed_orders * 100.0 / sessions,
    2
) AS conversion_rate

FROM fee_bucket

ORDER BY
CASE fee_bucket
WHEN '0-30' THEN 1
WHEN '30-50' THEN 2
WHEN '50-70' THEN 3
ELSE 4
END;