# -*- coding: utf-8 -*-
"""
Created on Wed Dec  3 10:06:12 2025

@author: thoma
"""
import sqlite3
from sqlite3 import Error
from project_config.config import db_database

def db_connectie():
    try:
        conn = sqlite3.connect(db_database)
        return conn
    except Error as e:
        print(f'Fout bij het connecteren met de database: {e}')
        