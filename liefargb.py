import mysql.connector
from mysql.connector import Error
from mysql.connector import errorcode

import os
import sys
import time
import pprint
import hashlib

from datetime import datetime

global now
connection = mysql.connector.connect(host='localhost', database='pe_parse_db', user='root', password='toor')

if __name__ == '__main__':
    try:
        filenamearg = sys.argv[1]
    except:
        print("Usage: python thispy.py <filenamearg>")
        sys.exit("Exit proses")

global exe_path
exe_path = filenamearg

sql_insert_query = """INSERT INTO `lief_pedump` (`md5`, `dump_string`) VALUES (%s, %s)"""

cursor = connection.cursor()
with open(exe_path,'r') as f2:
   fd = f2.read()
   val = (exe_path, fd)
   result = cursor.execute(sql_insert_query, val)
connection.commit()

print("Saved!")
