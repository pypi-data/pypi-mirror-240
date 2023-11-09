import os
import logging
from evydcloud.hive.connector import HiveConnector


class DBConnector:
    HIVE = 'hive'
    MYSQL = 'mysql'

    def __init__(self):
        self.db_type = os.environ.get('DB_TYPE') or self.HIVE
        self.logger = logging.getLogger("DbConnector")

    def create(self):
        conn_info = self._get_conn_info()
        if self.db_type == self.HIVE:
            hive_conn = HiveConnector()
            ret = hive_conn.connect(conn_info)
            if not ret:
                self.logger.error(f"Failed to create Hive connection by: {conn_info}.")
                return None
            return hive_conn
        else:
            raise NotImplementedError

    def _get_conn_info(self):
        conn_info = {}
        if self.db_type == self.HIVE:
            username = os.environ.get('JUPYTERHUB_USER')
            conn_info['username'] = username
            # get db conn info from business service

        return conn_info