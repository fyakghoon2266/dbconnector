# DB Connector Package

This Python package (`dbconnector`) provides a convenient way to connect to Teradata and Oracle databases. It includes error handling and uses SQLAlchemy for Oracle connections.

## Usage

### Teradata Connection

```python
# your_script.py

from dbconnector import connect_to_teradata

# Provide Teradata username and password
teradata_session = connect_to_teradata("your_teradata_username", "your_teradata_password")
if teradata_session:
    print("Connected to Teradata successfully.")
```



Oracle Connection
```python
# your_script.py

from dbconnector import connect_to_oracle

# Provide Oracle username, password, and connection string
oracle_connection = connect_to_oracle("your_oracle_username", "your_oracle_password")
if oracle_connection:
    print("Connected to Oracle successfully.")
```

Make sure to replace the placeholder values (your_teradata_username, your_teradata_password, your_oracle_username, your_oracle_password, localhost, 1521, ORCL) with your actual database credentials and connection details.

## Using the Package within Your Project
### Project Structure:

Your project should have a structure similar to the following:

```markdown
my_project/
├── dbconnector/
│   ├── __init__.py
│   ├── teradata_connector.py
│   └── oracle_connector.py
├── your_script.py
└── README.md
```

### Importing the Package:

In your main script (your_script.py), you can directly import the dbconnector package:

```python
# your_script.py

from dbconnector import connect_to_teradata, connect_to_oracle

# Other script logic...
```

### Connecting to Database and Reading Data:

Once connected successfully, you can use the pd.read_sql function from the Pandas library to read data from the database. Here's an example using Teradata:

```python
# your_script.py

import pandas as pd
from dbconnector import connect_to_teradata

# Connect to Teradata
teradata_session = connect_to_teradata("your_teradata_username", "your_teradata_password")

if teradata_session:
    print("Connected to Teradata successfully.")

    # Example: Read data from a table using pd.read_sql
    query = "SELECT * FROM your_teradata_table"
    df = pd.read_sql(query, teradata_session)
    print("Data from Teradata:")
    print(df)
```

And here's an example using Oracle:

``` python
# your_script.py

import pandas as pd
from dbconnector import connect_to_oracle

# Provide Oracle username, password, and connection string
oracle_connection = connect_to_oracle("your_oracle_username", "your_oracle_password")

if oracle_connection:
    print("Connected to Oracle successfully.")

    # Example: Read data from a table using pd.read_sql
    query = "SELECT * FROM your_oracle_table"
    df = pd.read_sql(query, oracle_connection)
    print("Data from Oracle:")
    print(df)
```

Make sure to replace your_teradata_table and your_oracle_table with the actual table names you want to query.

# Note
Ensure that your system has the necessary database drivers installed for Teradata and Oracle connections.
If you encounter any issues during installation or usage, check the error messages and verify your database credentials and connection details.
Happy coding!