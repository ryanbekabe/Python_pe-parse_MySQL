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

connection = mysql.connector.connect(host='localhost', database='pe_parse_db', user='root', password='Tamrun3571!')

if __name__ == '__main__':
    try:
        filenamearg = sys.argv[1]
    except:
        print("Usage: python thispy.py <filenamearg>")
        sys.exit("Exit proses")

#global now
#now = datetime.datetime.now()
global exe_path
exe_path = filenamearg
#exe_path = "cmd.exe"
fd = open(exe_path, 'rb')

path = "./exe2/"
arr = os.listdir(path)
arr.sort()
i=0
# for filenya in arr:
        # i=i+1
        # SAMPLE_FILE = filenya
        # print("File ke: " + str(i) + " | " + SAMPLE_FILE)
        # if not os.path.isdir(path + SAMPLE_FILE):
os.system("./dump-pe.so " + exe_path + " > " + exe_path + "_peparsedump");
with open(exe_path + "_peparsedump","rb") as f:
                bytes = f.read() # read file as bytes
                readable_hashmd5 = hashlib.md5(bytes).hexdigest();
                readable_hashsha256 = hashlib.sha256(bytes).hexdigest();
                print(readable_hashmd5)
                print(readable_hashsha256)
                md5nya = readable_hashmd5
                print("MD5nya = ",md5nya)
                sha256nya = readable_hashsha256
                print("SHA256nya = ",sha256nya)
                sql_insert_query = """INSERT INTO `pe-parse_pedump` (`md5`, `dump_string`) VALUES (%s, %s)"""
                val = (exe_path, bytes)
                cursor = connection.cursor()
                result = cursor.execute(sql_insert_query, val)
                connection.commit()
                print("Saved!")
