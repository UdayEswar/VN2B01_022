print("------Binary data formation-------")

adding = open(r"C:\Users\DELL\Desktop\Uday.jpg",'rb')
loading = open(r"C:\Users\DELL\Desktop\Pycharm Media\UdaySs_Img.jpg",'wb')

data = adding.read()
loading.write(data)

#adding.close()
adding.close()
print("-------------------------------")
print("========Pickling And Unpickling=========")
import pickle
#   pickle
my_list = ["uday","python"]     # list Type
with open("uday_pickling.txt",'wb') as file:
    #file.write("This is built with pickling")
    pickle.dump(my_list, file)
#   unpickle
unpic = open("uday_pickling.txt",'rb')
obj = pickle.load(unpic)
print("unpickle Data :",obj)

print("=====Seek=====")
#print("Here I Have one paragraph in this  para i Want only specific sentence")
with open("U_P.txt",'w') as file:
    file.write("A paragraph is a series of related sentences developing a central idea, called the topic. Try to think about paragraphs in terms of thematic.")
with open("U_P.txt",'r') as file_r:
    print("Before Seek :",file_r.read())
    print("Seek Value :",file_r.seek(15))
    print("Aftre Seek :",file_r.read())
print()
print("=====Tell=====")
k = open("U_P.txt",'r')
print("K :",k.read())
print("tell :",k.tell())
k.seek(40)
#k.read(30)
print("After Tell :",k.tell())






    #print("Tell :",file_r.tell())
    #print(file_r.read())
    #print("Tell :",file_r.tell())
    #print(file_r.read())















