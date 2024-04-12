# Data Engineering Challenge

## Problem Statement

Imagine you are working with a large dataset in a CSV file that contains information about sales transactions for the last month.
Pricing team has provided `sales_data.csv` CSV file that contains all the information.
Each row in the CSV file represents a single transaction, and the columns include information such as 
"TransactionID," "ProductID," "Quantity,", "SalePrice" and "PurchasePrice"

Your task is to:
### 1) Clean and Analyse the Dataset

* Create a Jupyter Notebook `data_analysis.ipynb` where you clean the dataset and analyze the relation between Sale Price and Quantity for some products.

* Save the cleaned dataset into `sales_data_cleaned.csv`.

### 2) Store Data into Database

* Prepare a docker compose file to run PostgreSQL.

* Implement a Python script `transfer_sales_data.py` to read `sales_data_cleaned.csv` and store the data into a table in the PostgreSQL database.

### 3) Implement Process Data Python Function

Implement a Python function (`process_data`) which performs the following transformations on the data:
* Calculate the total profit for each transaction by multiplying the "Quantity" and ("SalePrice" - "PurchasePrice") columns.
* Calculate the total profit for each product.
* Identify the top 2 selling products based on the **total quantity**.

The Python function `process_data(csv_file_path: str) -> tuple[dict[int, float], dict[int, float], list[int]]`
that reads the data from database and returns a tuple containing:

* A dictionary where the keys are transaction IDs, and values are the total profit for each transaction.
* A dictionary where the keys are product IDs, and values are the total profit for each product.
* The product IDs of the 2 top-selling products.

#### Example

Consider the following data in the database
```
transaction_id,product_id,quantity,sale_price,purchase_price
1,101,3,30.0,15.0
2,101,1,40.0,15.0
3,102,2,25.0,15.0
4,102,5,20.0,15.0
5,103,6,20.0,10.0
```
The function `process_data('sales_data.csv')` should return:
```
({
  1: 45.0,
  2: 25.0,
  3: 20.0,
  4: 25.0,
  5: 60.0
},{
  101: 70.0,
  102: 45.0,
  103: 60.0
},
[102, 103])
```

Ensure the function reads data from the PostgreSQL database and returns the desired results.

Please round floating results to 2 decimal places.

## Requirements

* Well structured code: Maintainable, Extensible and Readable.

* All three tasks are runnable locally on an isolated environment (e.g. Python virtual env or Docker container). We might ask you to change some part of your code in the interview. 

* The app.py should contain the implementation of the process_data function and any other necessary code.

* Include a requirements.txt file listing the Python packages needed for the application.

* Write necessary notes for each step of your solution in the README.md file.

* Prepare your solution with your favorite IDE and send your git repo as a zip file to us.


