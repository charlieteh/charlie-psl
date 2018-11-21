# -*- coding: utf-8 -*-
"""
Created on Mon Nov 19 10:37:13 2018

@author: Charles.Teh
"""

import sqlite3 as lite
import sys

con = None

try:
    con = lite.connect('data'testdb.db')
    cur - con.cursor()
    #cur.execute('SELECT SQLITE_VERSION')
    cur.execute('SELECT * from stuff')
    data = cure.fetchone()
    print(f'SQLite version')