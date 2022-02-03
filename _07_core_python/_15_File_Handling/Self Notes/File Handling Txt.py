print("----File Handling----")
                                            #   READ MODE
print("====.TXT File====")

print("\n----Read Mode----")
f = open('Uday.txt','r')
data = f.read()
print("Data From Uday File:",data)
f.close()

print("\n====Write====")                    #   WRITE MODE
f = open("Uday.txt",'w')
data = f.write("This is Uday")
print(data)
f.close()

print("\n====READ AFTER WRITE====")        #   READ MODE AFTER WRITE
f = open("Uday.txt",'r')
data = f.read()
print("This is After Write ::::",data)
f.close()

print("\n===APPEND===")                 #   APPEND
f = open("Uday.txt",'a')
data = f.write("\nUday is Everything")
print("'a'==> Append - will append to the end of the file ::",data)
f.close()

f = open("Uday.txt",'r')
data = f.read()
print(data)
f.close()
print()

print("=====HTML=====")
f = open("Uday_HTML.html",'r')
data = f.read()
print("HTML ::",data)
f.close()


print("\n======Outside Directory=======")           #   TXT FILE FROM OUTSIDE

print("===TXT FILE===")
f = open(r"C:\Users\DELL\Desktop\VN2B01_Training\_07_core_python\_15_File_Handling\write_data1.txt",'r')
data = f.read()
print("Text File From Other Directory ::",data)
f.close()

print("\n=====.CSV====")                            #   .CSV FILE FROM OUTSIDE
f = open(r"C:\Users\DELL\Desktop\VN2B01_Training\_07_core_python\_15_File_Handling\Self Notes\Uday_CSV.csv",'r')
data = f.read()
print(".CSV DATA ::",data)
f.close()

f = open(r"C:\Users\DELL\Desktop\VN2B01_Training\_07_core_python\_15_File_Handling\Self Notes\Uday_CSV.csv",'r')
data = f.read(20)
print(data)
f.close()
print()


f = open(r"C:\Users\DELL\Desktop\VN2B01_Training\_07_core_python\_15_File_Handling\Self Notes\Uday_CSV.csv",'r')
data = f.readline()
print(data)
data = f.readline()
print(data)
f.close()

f = open(r"C:\Users\DELL\Desktop\VN2B01_Training\_07_core_python\_15_File_Handling\Self Notes\Uday_CSV.csv",'r')
data = f.readlines(1)
print(data)
f.close()

f = open(r"C:\Users\DELL\Desktop\VN2B01_Training\_07_core_python\_15_File_Handling\Self Notes\Uday_CSV.csv",'r')
data = f.readlines(27)
print(data)
f.close()

f = open(r"C:\Users\DELL\Desktop\VN2B01_Training\_07_core_python\_15_File_Handling\Self Notes\Uday_CSV.csv",'r')
data = f.readlines(28)
print(data)
f.close()

f = open(r"C:\Users\DELL\Desktop\VN2B01_Training\_07_core_python\_15_File_Handling\Self Notes\Uday_CSV.csv",'a')
data = f.write("Gowtham : Kaza")
print(data)

f = open(r"C:\Users\DELL\Desktop\VN2B01_Training\_07_core_python\_15_File_Handling\Self Notes\Uday_CSV.csv",'r')
ap = f.read()
print(ap)
print()

f = open("Uday.txt",'r+')
data  = f.write("Adding Data Using 'R+'")
print('Form R+ ::',data)

f =open("Uday.txt",'r')
data = f.read()
print(data)
print()

print("Creating and Inserting In another file")


data_file = open("uday's data.txt",'r')
data_dipping_to = open("Adding data.txt",'w')

#data_file  = open("uday's data.txt",'r')
for data in data_file:
    data_dipping_to.write(data)







