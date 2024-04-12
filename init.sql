CREATE TABLE sales IF NOT EXISTS (
    transaction_id INT PRIMARY KEY,
    product_id INT,
    quantity INT,
    sale_price REAL
    purchase_price REAL
);