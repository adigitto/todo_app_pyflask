#!/usr/bin/env python3 
# -*- coding: utf-8 -*- 

import sqlite3 as lite
import sys

try:
  con = lite.connect('./todo_db_files/todo.db')
  cur = con.cursor()
  cur.execute("CREATE TABLE items (item TEXT NOT NULL PRIMARY KEY,status TEXT NOT NULL)")
  con.commit()

except Exception as e: 
  if con:
    con.rollback()
    print("Unexpected error %s:" % e.args[0]) 
    sys.exit(1) 

finally: 
    if con: 
        con.close()

