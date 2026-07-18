-- Funnel Analysis
-- Calculates the conversion at each stage of the QuickBite ordering funnel

SELECT
    COUNT(*) AS total_sessions,
    SUM(CASE WHEN restaurant_view THEN 1 ELSE 0 END) AS restaurant_views,
    SUM(CASE WHEN menu_view THEN 1 ELSE 0 END) AS menu_views,
    SUM(CASE WHEN cart THEN 1 ELSE 0 END) AS cart_additions,
    SUM(CASE WHEN checkout THEN 1 ELSE 0 END) AS checkouts,
    SUM(CASE WHEN payment THEN 1 ELSE 0 END) AS payments,
    SUM(CASE WHEN completed THEN 1 ELSE 0 END) AS completed_orders
FROM sessions;
