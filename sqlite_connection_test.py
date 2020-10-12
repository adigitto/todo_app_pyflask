"sqlite_connection_test.py" 23L, 522C
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sqlite3 as lite
import sys

try:
  con = lite.connect('products.db')
  cur = con.cursor()
  cur.execute("CREATE TABLE drinks(Id INTEGER PRIMARY KEY AUTOINCREMENT, Name TEXT, PRICE REAL)")
  cur.execute("CREATE TABLE fruits(Id INTEGER PRIMARY KEY AUTOINCREMENT, Name TEXT, Price REAL)")
  con.commit()

except Exception as e:
  if con:
    con.rollback()
    print("Unexpected error %s:" % e.args[0])
    sys.exit(1)

finally:
    if con:
        con.close()
