# CIS560Project

## Requirements

* Python3 installed.

* Pip3 installed.

### 1. Clone the repository

`git clone https://github.com/cata85/CIS560Project.git`

### 2. Install required packages

```bash
pip3 install flask
pip3 install pymssql
```

### 3. Run main.py

`python3 main.py`

### 4. View in browser

After running the command above there should be an <br /> 
output giving the path to view the webpage

### 5. Submission Notes

```
Tables:
All the Tables CREATE TABLE Queries are contained within each tables "file" within the data folder as part of a create_table method.

Data:
All the scripts used to populate the tables within the database are contained within the helpers.py file.
	def get_values pulls all our data from a JSON file into 2 variables called "default" and "init".
		default contained all necessary default values needed for the tables.
		init contains all the initial seed data so our table doesn't start empty.
	def insert_initial_values uses "init" and inserts all the seed data into our database.
		
Procedures/SQL Operations:
All SQL Queries and Operations are conducted in each of the tables "file" within the data folder.
The Report Queries are contained within the "ReportQueries.SQL" file within the Queries folder.

Other Routines:
No Views, Functions, or Triggers were used.

Application Code:
All other code and documentation exists within the CIS560Project folder.
```
