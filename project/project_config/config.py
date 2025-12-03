# -*- coding: utf-8 -*-
"""
Created on Wed Dec  3 09:35:16 2025

@author: thoma
"""

from environs import Env

env = Env()
env.read_env()

db_database = env.str("DB_DATABASE")