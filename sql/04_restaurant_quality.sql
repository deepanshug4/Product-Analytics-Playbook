SELECT
    CASE
        WHEN restaurant_rating < 3.5 THEN 'Below 3.5'
        WHEN restaurant_rating < 4.0 THEN '3.5 - 4.0'
        WHEN restaurant_rating < 4.5 THEN '4.0 - 4.5'
        ELSE '4.5+'
    END AS rating_bucket,

    COUNT(*) AS sessions,

    SUM(CASE WHEN completed THEN 1 ELSE 0 END) AS completed_orders,

    ROUND(
        100.0 * SUM(CASE WHEN completed THEN 1 ELSE 0 END) / COUNT(*),
        2
    ) AS conversion_rate

FROM sessions

GROUP BY 1

ORDER BY
CASE rating_bucket
    WHEN 'Below 3.5' THEN 1
    WHEN '3.5 - 4.0' THEN 2
    WHEN '4.0 - 4.5' THEN 3
    ELSE 4
END;