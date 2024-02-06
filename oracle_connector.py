from sqlalchemy import create_engine

import sys
import logging
import oracledb

oracledb.version = '8.3.0'
sys.modules['cx_Oracle'] = oracledb

def connect_to_oracle(username: str, password: str):
    if not username or not password:
        logging.info("Error: Username and password are required.")
        
        return None

    try:
        # 嘗試建立 Oracle 連線
        DB_DSN: str = "(DESCRIPTION=(ADDRESS_LIST=(ADDRESS=(PROTOCOL=tcp)(PORT=1521)(HOST=tdctomracl3-scan.cathayuat.intra.uwccb)))(CONNECT_DATA=(SERVICE_NAME=OIRBSRV)))"
        connection = create_engine(
            f"oracle://{username}:{password}@{DB_DSN}",
            echo=False
        )
        
        return connection

    except Exception as e:
        # 處理 Oracle 連線錯誤
        logging.error(f"Oracle Connection Error: {str(e)}")
        
        return None