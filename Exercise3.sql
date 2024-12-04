-- Exercise 3.1: Data Retrieval and Aggregation
-- Question 1 : Retrieve the top 5 customers who have made the highest total purchase amount.
SELECT 
    c.name,
    SUM(oi.quantity * oi.price) AS total_purchase_amount
FROM Customers c
JOIN Orders o ON c.customer_id = o.customer_id
JOIN OrderItems oi ON o.order_id = oi.order_id
GROUP BY c.name
ORDER BY total_purchase_amount DESC
LIMIT 5;



-- Exercise 3.2: Data Modification and Transaction
-- Question 2 : Transaction to cancel John Doe's most recent order.
BEGIN TRANSACTION;

-- Delete order items for the most recent order by John Doe
DELETE FROM OrderItems
WHERE order_id = (
    SELECT o.order_id
    FROM Orders o
    JOIN Customers c ON o.customer_id = c.customer_id
    WHERE c.name = 'John Doe'
    ORDER BY o.order_date DESC
    LIMIT 1
);

-- Delete the most recent order by John Doe
DELETE FROM Orders
WHERE order_id = (
    SELECT o.order_id
    FROM Orders o
    JOIN Customers c ON o.customer_id = c.customer_id
    WHERE c.name = 'John Doe'
    ORDER BY o.order_date DESC
    LIMIT 1
);

COMMIT;



-- Exercise 3.3: Schema Modification and Indexing
-- Question 3: Add a new column "category" to the Products table.
ALTER TABLE Products 
ADD category VARCHAR(255);

-- Question 4 : Explanation of columns in Customers and Products tables that should be indexed

-- Columns that are good candidates for indexing are typically:
-- 1. Columns with mostly unique values
-- 2. Columns frequently used in WHERE clauses, ORDER BY clauses, or JOIN conditions

-- Customers Table:
-- customer_id: 
--    - This is the primary key of the Customers table and is automatically indexed.
--    - It uniquely identifies each customer and is used in JOIN operations with the Orders table (as seen above).
-- email:
--    - This column contains unique values for each customer and may be frequently queried.
--    - For example, we might search for a customer by email during authentication or validation.
--    - Indexing this column improves query performance for such lookups.

-- Products Table:
-- product_id:
--    - This is the primary key of the Products table and is automatically indexed.
--    - It uniquely identifies each product and can be used in JOIN operations with the OrderItems table.
-- category:
--    - If we frequently filter or search products by their category, indexing this column improves query performance.
--    - For example, a query like "SELECT * FROM Products WHERE category = 'Electronics'" would benefit significantly from an index.