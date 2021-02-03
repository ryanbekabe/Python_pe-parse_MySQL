import os
import sys

path = "./exe2/"
arr = os.listdir(path)
arr.sort()
i=0
for filenya in arr:
        i=i+1
        SAMPLE_FILE = filenya
        print("File ke: " + str(i) + " | " + SAMPLE_FILE)
        if not os.path.isdir(path + SAMPLE_FILE):
                os.system("python3 peparsearg.py " + path + SAMPLE_FILE);
# + " > " + SAMPLE_FILE + "_peparsedump");
