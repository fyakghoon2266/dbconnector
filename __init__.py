import subprocess
import logging

required_packages = ['sqlalchemy_teradata']

sqlalchemy_version = '1.3.24'
cx_oracle_version = '8.3.0'

required_packages.append(f'cx_Oracle=={cx_oracle_version}')
required_packages.append(f'sqlalchemy=={sqlalchemy_version}')

try:
    for package in required_packages:
        __import__(package)

except ImportError:
    logging.info('Installing required packages...')
    subprocess.run(['pip', 'install', *required_packages])

from .teradata_connector import connect_to_teradata
from .oracle_connector import connect_to_oracle