SELECT
    CASE
        WHEN coupon_used THEN 'Coupon Used'
        ELSE 'No Coupon'
    END AS coupon_group,

    COUNT(*) AS total_orders,

    ROUND(AVG(basket_value), 2) AS avg_basket_value,

    ROUND(AVG(discount), 2) AS avg_discount,

    ROUND(AVG(total_paid), 2) AS avg_total_paid,

    ROUND(AVG(customer_rating), 2) AS avg_customer_rating

FROM orders

GROUP BY coupon_used

ORDER BY coupon_used DESC;