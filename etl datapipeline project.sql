CREATE DATABASE ecommerce_db;
USE ecommerce_db;

USE ecommerce_db;

CREATE TABLE orders (
    order_id INT PRIMARY KEY,
    order_date DATE,
    customer_name VARCHAR(100),
    city VARCHAR(50),
    product VARCHAR(100),
    category VARCHAR(50),
    quantity INT,
    price DECIMAL(10,2)
);

/*select*from orders;*/

/*total orders query*/
SELECT COUNT(*) AS total_orders
FROM orders;

/* total revenue */
SELECT SUM(quantity * price) AS total_revenue
FROM orders;

/* city wise sales */
SELECT city,
       SUM(quantity * price) AS total_sales
FROM orders
GROUP BY city
ORDER BY total_sales DESC;

/* product wise sales */

SELECT product,
       SUM(quantity) AS total_quantity,
       SUM(quantity * price) AS total_sales
FROM orders
GROUP BY product
ORDER BY total_sales DESC;