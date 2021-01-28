path = "./exe/"
arr = os.listdir(path)
arr.sort()
i=0
for filenya in arr:
        i=i+1
        SAMPLE_FILE = filenya
        print("File ke: " + str(i) + " | " + SAMPLE_FILE)
        if not os.path.isdir(path + SAMPLE_FILE):
                os.system("python3 pefiledump2.py " + path + SAMPLE_FILE + " > " + SAMPLE_FILE + "_pefiledump");
                with open(SAMPLE_FILE + "_dump","rb") as f:
                        bytes = f.read() # read file as bytes
