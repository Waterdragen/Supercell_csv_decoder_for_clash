import os, ctypes, lzma

def decode_file(path):
    basename = os.path.splitext(path)[0]+"_temp.csv"
    directory = os.path.join("In-csv",basename)
    decodedname = os.path.join("Out-csv", os.path.basename(path))
    with open(directory, 'rb') as f:
        data = f.read()
    tempdata = bytearray()
    for i in range(0, 8):
        tempdata.append(data[i])
    for i in range(0, 4):
        tempdata.append(0)
    for i in range(8, len(data)):
        tempdata.append(data[i])
    try:
        with open(decodedname, 'wb') as f:
            decompressor = lzma.LZMADecompressor()
            unpack_data = decompressor.decompress(tempdata)
            f.write(unpack_data)
            os.remove(directory)
    except:
        print("^---invalid input")

ctypes.windll.kernel32.SetConsoleTitleW("Supercell csv decoder for clash")
directory_in = 'In-csv'
directory_out = 'Out-csv'
if not os.path.exists(directory_in):
    os.makedirs(directory_in)
if not os.path.exists(directory_out):
    os.makedirs(directory_out)
print('Here are your .csv files:\n')
for filename in os.listdir(directory_in):
    f = os.path.join(directory_in, filename)
    if os.path.isfile(f) and filename.endswith(".csv"):
        file = open(f,"rb")
        with open(f, 'rb') as csvbin:
            s = csvbin.read()
        with open('keyword.txt', 'rb') as keyword:
            search_str = keyword.read().rstrip()
        found = s.find(search_str)
        base = os.path.basename(f)
        space_num = 34-len(base)
        i=0
        space=''
        for i in range(space_num):
            space=space+' '
        if found == 0:
            print(base,space,'---- Decode')   #Require decoding afterwards
        elif found != -1:
            print(base,space,'---- Trim+Decode')  #Trimmed, require decoding afterwards
        else:
            print(base,space,'---- OK')   #Can be directly opened by csv editor
        if found != -1:
            complete_name = os.path.join(directory_in,os.path.splitext(base)[0])+'_temp.csv'
        else:
            complete_name = os.path.join(directory_out, os.path.splitext(base)[0]) + '.csv'
        newfile = open(complete_name, "wb")
        byte = file.read(1)
        i=0
        while byte:
            if i >= found:
                newfile.write(byte)
            else:
                i += 1
            byte = file.read(1)
        file.close()
        newfile.close()
        if found != -1:
            decode_file(filename)
input("\nDecoded .csv saved to Out-csv \nPress Enter to exit")
#My first modding script :P @Waterdragen