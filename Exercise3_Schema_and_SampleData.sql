-- Initialize database schema
CREATE TABLE Customers (
  customer_id INT PRIMARY KEY,  -- Primary key to uniquely identify customers
  name VARCHAR(100) NOT NULL,   -- Customer name
  email VARCHAR(255) UNIQUE,    -- Ensuring email addresses are unique
  created_at DATE NOT NULL      -- Date when the customer was created
);

CREATE TABLE Orders (
  order_id INT PRIMARY KEY,     -- Primary key for orders
  customer_id INT NOT NULL,     -- Foreign key to link to Customers
  order_date DATE NOT NULL,     -- Date when the order was placed
  FOREIGN KEY (customer_id) REFERENCES Customers(customer_id) -- Enforce relationship
);

CREATE TABLE OrderItems (
  order_item_id INT PRIMARY KEY,   -- Primary key for order items
  order_id INT NOT NULL,           -- Foreign key to link to Orders
  product_id INT NOT NULL,         -- Foreign key to link to Products
  quantity INT NOT NULL,           -- Quantity of the product in the order
  price FLOAT NOT NULL,            -- Price of the product in the order
  FOREIGN KEY (order_id) REFERENCES Orders(order_id),    -- Enforce relationship
  FOREIGN KEY (product_id) REFERENCES Products(product_id) -- Enforce relationship
);

CREATE TABLE Products (
  product_id INT PRIMARY KEY,      -- Primary key for products
  name VARCHAR(100) NOT NULL,      -- Product name
  description VARCHAR(255),        -- Optional description of the product
  price FLOAT NOT NULL             -- Price of the product
);


-- Insert Sample Data
INSERT INTO Customers (customer_id, name, email, created_at)
VALUES
    (1, 'John Doe', 'john@example.com', '2023-01-01'),
    (2, 'Jane Smith', 'jane@example.com', '2023-02-01'),
    (3, 'Alice Brown', 'alice@example.com', '2023-02-15'),
    (4, 'Bob White', 'bob@example.com', '2023-03-01'),
    (5, 'Charlie Green', 'charlie@example.com', '2023-03-10'),
    (6, 'David Black', 'david@example.com', '2023-03-15');

INSERT INTO Orders (order_id, customer_id, order_date)
VALUES
    (1, 1, '2023-03-01'),
    (2, 1, '2023-03-05'),
    (3, 2, '2023-03-02'),
    (4, 3, '2023-03-05'),
    (5, 4, '2023-03-07'),
    (6, 5, '2023-03-09'),
    (7, 6, '2023-03-10');

INSERT INTO OrderItems (order_item_id, order_id, product_id, quantity, price)
VALUES
    (1, 1, 101, 2, 50.0), 
    (2, 1, 103, 3, 80.0), 
    (3, 2, 102, 1, 100.0), 
    (4, 3, 101, 4, 50.0), 
    (5, 4, 102, 2, 100.0), 
    (6, 5, 101, 5, 50.0), 
    (7, 6, 103, 3, 80.0), 
    (8, 7, 101, 6, 50.0); 

INSERT INTO Products (product_id, name, description, price)
VALUES
    (101, 'Widget A', 'Description A', 50.0),
    (102, 'Widget B', 'Description B', 100.0),
    (103, 'Widget C', 'Description C', 80.0); 
