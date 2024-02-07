import subprocess
import logging
import sys

class DBConnector:
    def __init__(self):
        self.logger = logging.getLogger(__name__)

    def install_package_if_needed(self, package):
        try:
            self.logger.info(f"Installing required package: {package}")
            subprocess.run(['pip', 'install', package])
        except ImportError:
            self.logger.info(f"Installing required package: {package}")
            subprocess.run(['pip', 'install', package])

    def install_required_packages(self):
        sqlalchemy_version = '1.3.24'
        oracledb_version = '1.2.2'
        required_packages = ['sqlalchemy_teradata', f'oracledb=={oracledb_version}', f'sqlalchemy=={sqlalchemy_version}']
        for package in required_packages:
            self.install_package_if_needed(package)

    def connect_to_teradata(self, username, password):
        self.install_required_packages()

        from sqlalchemy import create_engine

        if not username or not password:
            logging.info("Error: Username and password are required.")
            
            return None

        try:
            # 嘗試建立 Teradata 連線
            # uda_exec = teradata.UdaExec(appName="DBConnector", version="1.0", logConsole=False)
            # session = uda_exec.connect(method="odbc", system="your_teradata_system", username=username, password=password)

            engine = create_engine(f'teradata://{username}:{password}@88.8.98.214/VP_MCIF')
            connection = engine.connect()
            logging.info('Teradata Connection Success')

            return connection

        except Exception as e:
            # 處理 Teradata 連線錯誤
            logging.error(f"Teradata Connection Error: {str(e)}")
            return None
        

    def connect_to_oracle(self, username, password, connection_string):
        self.install_required_packages()

        from sqlalchemy import create_engine
        import oracledb

        oracledb.version = '8.3.0'
        sys.modules['cx_Oracle'] = oracledb

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
            logging.info('Oracle Connection Success')

            return connection

        except Exception as e:
            # 處理 Oracle 連線錯誤
            logging.error(f"Oracle Connection Error: {str(e)}")
            
            return None

# Automatically install required packages if the user directly runs the script
if __name__ == "__main__":
    db_connector = DBConnector()
    db_connector.install_required_packages()