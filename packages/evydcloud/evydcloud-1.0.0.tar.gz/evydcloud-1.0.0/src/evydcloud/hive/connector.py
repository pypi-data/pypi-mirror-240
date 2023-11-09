from evydcloud.connector_base import ConnectorBase
import pandas as pd
import logging
from pyhive import presto

class HiveConnector(ConnectorBase):
    def __init__(self):
        self.conn = None
        self.logger = logging.getLogger("HiveConnector")

    def connect(self, conn_info):
        if not conn_info:
            self.logger.error("There is no valid conn info to create hive connection.")
            return False
        _host = conn_info.get("host")
        _port = conn_info.get("port")
        _user_name = conn_info.get("username")
        try:
            self.conn = presto.connect(host=_host, port=_port, username=_user_name)
        except Exception as ecp:
            self.logger.error(str(ecp))
            return False
        return True

    def query(self, sql):
        if not self.conn:
            raise Exception("Not created a valid hive connection yet.")
        if not sql:
            self.logger.warn("There is no sql input.")
            return None
        df = pd.read_sql(self.conn, sql)
        return df
