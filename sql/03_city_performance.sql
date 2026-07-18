SELECT
    city,
    COUNT(*) AS sessions,
    SUM(CASE WHEN completed THEN 1 ELSE 0 END) AS completed_orders,
    ROUND(
        100.0 * SUM(CASE WHEN completed THEN 1 ELSE 0 END) / COUNT(*),
        2
    ) AS conversion_rate,
    ROUND(AVG(delivery_fee), 2) AS avg_delivery_fee
FROM sessions
GROUP BY city
ORDER BY conversion_rate DESC;