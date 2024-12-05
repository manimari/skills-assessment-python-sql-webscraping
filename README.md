# Skills Assessment Test - Python, SQL, Web Scraping

This repository contains solutions to a skills assessment test involving Python, SQL, and Web Scraping tasks. Below are the details of the tasks and the solutions implemented in this repository.

## Exercises Overview:

### Section 1: Python

#### Exercise 1: Find Duplicate Numbers
- **File:** `Exercise1.py`
- **Description:** A Python function that takes a list of integers as input and returns a list of all the numbers that appear more than once.
- **Example Input:** `[1, 2, 3, 2, 4, 5, 4, 6]`
- **Example Output:** `[2, 4]`

#### Exercise 2: File Handling and Data Manipulation
- **File:** `Exercise2.py`
- **Description:** A Python program that reads student names and their grades from a file (`grades.txt`), stores it in a dictionary, and calculates the average grade.
- **Input File:** `grades.txt`
- **Example Output:** The average grade is printed after reading the file data.

### Section 2: SQL

#### Exercise 3: Sales Database
- **File:** `Exercise3.sql`
- **Description:** SQL queries to retrieve and modify data in a sales database, including customer purchase data, order cancellations, and database schema modification.

1. **Data Retrieval and Aggregation:**
   - Retrieve the top 5 customers with the highest total purchase amounts.
   
2. **Data Modification and Transaction:**
   - Cancel the most recent order for a customer named "John Doe."

3. **Schema Modification and Indexing:**
   - Add a new `category` column to the `Products` table.
   - Explanation of indexing for key columns in the `Customers` and `Products` tables.

### Section 3: Web Scraping

#### Exercise 6: Web Scraping UK Prime Ministers
- **File:** `Exercise6.py`
- **Description:** A Python program using `requests`, `BeautifulSoup`, and `pandas` to scrape a list of UK Prime Ministers, their birthdates, and political affiliations from the Britannica website.
- **Output:** The data is saved in two Excel files: 
    1. `uk_prime_ministers.xlsx`: Contains the scraped data with duplicate rows.
    2. `uk_prime_ministers_deduplicated.xlsx`: Contains the scraped data without duplicate rows.
- **Note:** Some entries in the "Date of Birth" column on the source website include only the year (e.g., "1696") or an incomplete date with uncertainty (e.g., "1673?"). These entries were left blank in the Excel file because they could not be transformed into the required date format (dd.mm.yyyy). This ensures data consistency and avoids misleading transformations.

### Files in the Repository:
- **`Exercise1.py`**: Solution to find duplicate numbers in a list.
- **`Exercise2.py`**: Solution for reading student grades from a file and calculating the average.
- **`Exercise3.sql`**: SQL queries for data retrieval, modification, and schema alteration in a sales database.
- **`Exercise3_Schema_and_SampleData.sql`**: SQL schema and sample data for the sales database (for Exercise 3).
- **`Exercise6.py`**: Web scraping solution to extract UK Prime Ministers' data.
- **`grades.txt`**: Input file containing student names and grades (for Exercise 2).
- **`uk_prime_ministers.xlsx`**: Output Excel file containing the scraped UK Prime Ministers' data with duplicates included. 
- **`uk_prime_ministers_deduplicated.xlsx`**: Output Excel file containing the scraped UK Prime Ministers' data without duplicates.

## How to Run the Code:

### Python Solutions:
1. Make sure you have Python 3.6+ installed.
2. Install the required libraries by running: 
```
pip install requests beautifulsoup4 pandas
``` 
3. To run the Python exercises:
- For Exercise 1: Run `python Exercise1.py`.
- For Exercise 2: Run `python Exercise2.py` (ensure `grades.txt` is in the same directory).
- For Exercise 6: Run `python Exercise6.py` (this will create an Excel file `uk_prime_ministers.xlsx`).

### SQL Solutions:
1. The SQL queries in `Exercise3.sql` should be executed in any SQL database system that supports standard SQL syntax. Alternatively, you can use an online SQL editor like [MyCompiler SQL](https://www.mycompiler.io/new/sql) if you prefer not to set up a local database.
2. Use `Exercise3_Schema_and_SampleData.sql` to create the database schema and insert sample data before running the queries.