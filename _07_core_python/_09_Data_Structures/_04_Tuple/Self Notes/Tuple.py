
List = [11,22,33]       #This Is List, [] Mutable
Tuple = (11,22,33)      #This Is Tuble () Immutable
print(type(List),type(Tuple))

print("          -----Tuple-----")
print("          ===Indexing===")
Tuple = (1,2,3,4,5,6,7,8)
print("Before :",Tuple)
print("After :",Tuple[2])

print("          ===Slicing===")
print("Before :",Tuple)
print("After :",Tuple[2:5])

print("          +++Adding+++")
Tuple2 = (99,88,77)
print("Before :",Tuple,Tuple2)
print("After :",Tuple+Tuple2)
T_Add=Tuple+Tuple2
print("Adding Diff Way :",T_Add)

print("          ***Multiply***")
print("Before :",Tuple)
print("After :",Tuple*2)

print("           ///Membership///")
print("Before :",Tuple)
print("After :",5 in Tuple)
print("For -Ve Ans :",9 in Tuple)

print("           ---Length---")
print("Before :",Tuple)
print("After :",len(Tuple))

print("           ---Max---")
print("Before :",Tuple)
print("After :",max(Tuple))

print("            ---Min---")
print("Before :",Tuple)
print("After :",min(Tuple))

print("            @@@Immutable@@@")
#print("Before :",Tuple)
#Tuple.append(555)
#print("After :",Tuple)
Tuple3=(1,2,3,4,5,[11,22,33],6)
print("Before :",Tuple3)
Tuple3[5].append(555)
print("After :",Tuple3)





