import datetime
import hashlib
import mmap
import pefile
import pymysql
import sys
import time
pymysql.install_as_MySQLdb()

import MySQLdb
db = MySQLdb.connect(user="root",passwd="toor",host="localhost",db="pe_parse_db")
cursor = db.cursor()

if __name__ == '__main__':
    try:
        filenamearg = sys.argv[1]
    except:
        print("Usage: python thispy.py <filenamearg>")
        sys.exit("Exit proses")



global now
now = datetime.datetime.now()
global exe_path
exe_path = filenamearg
#exe_path = "cmd.exe"
fd = open(exe_path, 'rb')
pePath = pefile.PE(exe_path)
pe_data = mmap.mmap(fd.fileno(), 0, access=mmap.ACCESS_READ)
pe = pefile.PE(data=pe_data) #mode lambat full dump data
#pe = pefile.PE(data=pe_data, fast_load=True) #mode cepat mini dump data
global strpe
strpe = str(pe)

hasher = hashlib.md5()
hashersha256 = hashlib.sha256()
with open(exe_path, 'rb') as afile:
    buf = afile.read()
    hasher.update(buf)
    hashersha256.update(buf)
#print(hasher.hexdigest())
#print(hashersha256.hexdigest())

def file_size(fname):
    import os
    statinfo = os.stat(fname)
    return statinfo.st_size

cursor.execute("INSERT INTO pefile_pedump VALUES (NULL, %s, %s, %s, %s, %s, %s)", (exe_path, hasher.hexdigest(), hashersha256.hexdigest(), file_size(exe_path), strpe, now))
data=cursor.fetchall()

global pesection
for section in pe.sections:
    pesection = section.Name.decode('utf-8') + " - " + hex(section.Misc_VirtualSize) + " - " + hex(section.VirtualAddress) + " - " + hex(section.SizeOfRawData) #, section.Name, hex(section.VirtualAddress),hex(section.Misc_VirtualSize), section.SizeOfRawData
    #print(pesection)
    #cursor.execute("INSERT INTO pefile_pedump VALUES (NULL, %s, %s, %s, %s, %s, %s)", (exe_path, hasher.hexdigest(), hashersha256.hexdigest(), file_size(exe_path), pesection, now))
    #data=cursor.fetchall()

def foo(dll):
        cursor.execute("INSERT INTO pefile_pedump VALUES (NULL, %s, %s, %s, %s, %s, %s)", (exe_path, hasher.hexdigest(), hashersha256.hexdigest(), file_size(exe_path), dll, now))
        data=cursor.fetchall()

#i = 0
for resource_type in pePath.DIRECTORY_ENTRY_RESOURCE.entries:
        if resource_type.name is not None:
                name = "%s" % resource_type.name
                #print(name)
                #cursor.execute("INSERT INTO pedump VALUES (NULL, %s, %s, %s, %s, %s, %s)", (exe_path, hasher.hexdigest(), hashersha256.hexdigest(), file_size(exe_path), name, now))
        else:
                name = "%s" % pefile.RESOURCE_TYPE.get(resource_type.struct.Id)
                #print(name)
                #cursor.execute("INSERT INTO pedump VALUES (NULL, %s, %s, %s, %s, %s, %s)", (exe_path, hasher.hexdigest(), hashersha256.hexdigest(), file_size(exe_path), name, now))
        if name == None:
                name = "%d" % resource_type.struct.Id
                #print(name)
        if hasattr(resource_type, 'directory'):
                for resource_id in resource_type.directory.entries:
                        if hasattr(resource_id, 'directory'):
                                for resource_lang in resource_id.directory.entries:
                                        data = pePath.get_data(resource_lang.data.struct.OffsetToData, resource_lang.data.struct.Size)
                                        #print(data)
                                        #filetype = get_filetype(data)
                                        lang = pefile.LANG.get(resource_lang.data.lang, '*unknown*')
                                        #print(lang)
                                        sublang = pefile.get_sublang_name_for_lang( resource_lang.data.lang, resource_lang.data.sublang )
                                        #print(sublang)
                                        #ret[i] = (name, resource_lang.data.struct.OffsetToData, resource_lang.data.struct.Size, filetype, lang, sublang)
                                        #i += 1

#print("[*] Listing imported DLLs...")
for entry in pePath.DIRECTORY_ENTRY_IMPORT:
        global dll
        dll = '\t' + entry.dll.decode('utf-8')
        #foo(dll)

db.close()
