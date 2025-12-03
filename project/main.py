# -*- coding: utf-8 -*-
"""
Created on Wed Dec  3 09:47:01 2025

@author: thoma
"""

import pandas as pd
import sqlite3
from sqlite3 import Error
from service.service import db_connectie
from models import car

conn = db_connectie()
cur = conn.cursor()
query ='''
select * 
from cars
'''
data = pd.read_sql_query(query, conn)
print(data)
conn.close()