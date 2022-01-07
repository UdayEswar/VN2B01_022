'''
# Builtin functions:
---------------------
append insert extend   : UPDATE
pop  remove            : DELETE
count                  : RETRIEVE
index                  : RETRIEVE
reverse                : UPDATE
sort                   : UPDATE
copy                   : CREATE
'''

print("--------List Functions--------")
print("\n1.       ===Append===")
list = [1,2,3,4,5]          # Append
print("Before :",list)
list.append("Uday")
list.append(True)
list.append({5:5})
print("After :",list)

print("\n2.       ===Extend===")
list=[1,2,3,4,5]
print("Before :",list)
list.extend((50,60,70))
print("After :",list)

print("\n3.       ====Insert===")
list=[1,2,3,4,5]
print("Before :",list)
list.insert(1,4+3)
print("After :",list)

print("\n4.       ====P0P===")
list=[11,22,44,33,55]
print("Befor :",list)
list.pop(1)
print("After :",list)
list.pop()
print("Without Any Sp Index :",list)

print("\n5.       ===Remove===")
list=[99,88,77,55]
print("Before :",list)
list.remove(77)
print("After :",list)

print("\n6.       ===Insert[Index,obj]")
list=[55,6,44,88,99]
print("Before :",list)
list[1]=111
print("After :",list)
list.insert(1,222)
print("After Insert :",list)

print("\n7.          ===Count===")
list=[11,22,33,44,33,33,33,55,66,77]
print("Before :",list)
a=list.count(33)
print("After :",a)

print("\n8.          ===Index===")
list=[12,13,14,15,16]
print("Before :",list)
a=list.index(14)
print("After :",a)

print("\n9.         ===Reverse===")
list=[11,22,33,44,55,66]
print("Before :",list)
list.reverse()
print("After :",list)

print("\n10.        ===Sort===")
list=[99,55,88,44,33,11,77,66,22,]
print("Before :",list)
list.sort()
print("After  :",list)

print("\n11.         ===Copy===")
list=[1,2,3,4,5,6]
print("Before :",list)
a=list.copy()
print("After :",a)

b=list
b.append(999)
print("After :",b)




