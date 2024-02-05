import cx_Oracle
import logging


def connect_to_oracle(username, password):
    if not username or not password:
        logging.info("Error: Username and password are required.")
        return None

    try:
        # 嘗試建立 Oracle 連線
        connection = cx_Oracle.connect(username, password, "your_oracle_connection_string")
        return connection
    except cx_Oracle.Error as e:
        # 處理 Oracle 連線錯誤
        logging.info(f"Oracle Connection Error: {str(e)}")
        return None