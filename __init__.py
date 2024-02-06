import subprocess
import logging

required_packages = ['sqlalchemy_teradata']

sqlalchemy_version = '1.3.24'
oracledb_version = '1.2.2'

required_packages.append(f'oracledb=={oracledb_version}')
required_packages.append(f'sqlalchemy=={sqlalchemy_version}')

try:
    for package in required_packages:
        __import__(package)

except ImportError:
    logging.info('Installing required packages...')
    subprocess.run(['pip', 'install', *required_packages])

from .teradata_connector import connect_to_teradata
from .oracle_connector import connect_to_oracle