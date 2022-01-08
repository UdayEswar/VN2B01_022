print("                 ---Function---")
List = [11,22,33,44,55]
print("Before :",List,type(List))
Tuple = tuple(List)
print("After :",Tuple,type(Tuple))

Tuple = (99,88,77,44,55,66,)
print("Iterate The Loop")
for i in Tuple:
    print(Tuple)

Len = len(Tuple)
for i in range(Len):
    print(i,":",Tuple[i])

Tuple = (111,444,333,555,888,444)
print("Before :",Tuple,"Len :",len(Tuple))
for i in range(len(Tuple)):
    if Tuple[i] == 333:
        print("After '(Index Value)' :",i)
print()
print("Count :",Tuple.count(444))
print("Index :",Tuple.index(888))
print()
print("         *-*-*-P0P AND REMOVE*-*-*-")
print("Before :",List)
List.remove(44)
print("After_Remove :",List)




