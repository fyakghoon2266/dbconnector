from sqlalchemy import create_engine
import sqlalchemy_teradata
import logging

def connect_to_teradata(username, password):
    if not username or not password:
        logging.info("Error: Username and password are required.")
        return None

    try:
        # 嘗試建立 Teradata 連線
        # uda_exec = teradata.UdaExec(appName="DBConnector", version="1.0", logConsole=False)
        # session = uda_exec.connect(method="odbc", system="your_teradata_system", username=username, password=password)

        engine = create_engine(f'teradata://{username}:{password}@teradata_server/database')
        connection = engine.connect()
        return connection
    except Exception as e:
        # 處理 Teradata 連線錯誤
        logging.info(f"Teradata Connection Error: {str(e)}")
        return None