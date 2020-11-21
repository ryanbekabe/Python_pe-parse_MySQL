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
#os.system("./dump-pe.so exe/smadav1416.update >> dump_smadav1416.txt");

WINLE = b'\r\n'
ULE = b'\n'
#file_path = r"wintolin.txt"


path = "exe\\"
arr = os.listdir(path)
i=0
for filenya in arr:
	i=i+1
	SAMPLE_FILE = filenya
	print("File ke: " + str(i) + " | " + SAMPLE_FILE)
	if not os.path.isdir(path + SAMPLE_FILE):
		os.system("dump-pe.exe " + path + SAMPLE_FILE + " > " + SAMPLE_FILE + "_dump");
		#with open("dump_smadav1416.txt","rb") as f:
		file_path = SAMPLE_FILE + "_dump"
		with open(file_path, 'rb') as open_file:
			content = open_file.read()

		content = content.replace(WINLE, ULE)
		with open(file_path, 'wb') as open_file:
			open_file.write(content)
   
		with open(SAMPLE_FILE + "_dump","rb") as f:
			bytes = f.read() # read file as bytes
			readable_hashmd5 = hashlib.md5(bytes).hexdigest();
			readable_hashsha256 = hashlib.sha256(bytes).hexdigest();
			print(readable_hashmd5)
			print(readable_hashsha256)
			md5nya = readable_hashmd5
			print("MD5nya = ",md5nya)
			sha256nya = readable_hashsha256
			print("SHA256nya = ",sha256nya)
			sql_insert_query = """INSERT INTO `tbdumpwindows` (`md5`, `dump_string`) VALUES (%s, %s)"""
			val = (SAMPLE_FILE, bytes)
			cursor = connection.cursor()
			result = cursor.execute(sql_insert_query, val)
			connection.commit()
			print("Saved!")
