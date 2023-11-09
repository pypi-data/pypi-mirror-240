#!/usr/bin/env python
#encoding=utf-8
#@Author: yingjie.wang@yiducloud.cn, 2021, all rights reserved 
#@Created on 2023-10-30
#@Brief: DB Connector Base
from abc import ABC, abstractmethod

class ConnectorBase(ABC):
    @abstractmethod
    def connect(self, conn_info):

        return True

    @abstractmethod
    def query(self, sql):
        return None
