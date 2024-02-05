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