-- Query 5
SELECT product_name, round((sales_price - purchase_price)*0.07,2) profit_margin FROM Products ORDER BY profit_margin DESC, product_name;

-- Query 6
SELECT customer_id, round(purchased_items/carted_items*100,2) purchased_percentage FROM Shopping_Cart ORDER BY purchased_percentage DESC;

SELECT customer_id FROM Shopping_Cart ORDER BY customer_id DESC;

-- Query 7
SELECT *, (car_price*cars_sold)-production_cost profit FROM Tesla_Models;

-- Query 8
select * from Students where grade REGEXP 'A|B' order by first_name, last_name;

-- Query 9
select count(*) from customers where age > 65 OR total_purchase > 200;

-- Query 10
select * from Patient where age>50 and cholesterol >=240 and weight>=200 order by cholesterol DESC;