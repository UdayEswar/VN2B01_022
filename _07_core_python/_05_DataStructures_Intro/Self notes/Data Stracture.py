# Index Value

'''
Uday Eswar==>0(U),1(d),2(a),3(y),4(),5(E),6(s),7(w),8(a),9(r)
Uday Eswar==>-10(U),-9(d),-8(a),-7(y),-6(),-5(E),-4(s),-3(w),-2(a),-1(r)
'''

# +ve Values

name="Uday Eswar"
print (name)
print ("----(+Ve Value)----")
print ("0th index Value :",name[0])
print ("1th index Value :", name[1])
print ("2th index Value :", name[2])
print ("3th index Value :", name[3])

# -ve Values
print ("\n----(-Ve Value)----")
print ("-5th index Value :",name[-5])
print ("-4th index Value :",name[-4])
print ("-3th index Value :",name[-3])
print ("-2th index Value :",name[-2])
print ("-1th index Value :",name[-1])

# List
print ("\n------LIST------")

list=[143,14.3,"VasuDev",[1,4,3],(3,4,1),{1:43,3:41},{2-1,5-1,6-3,}]
print (list)
print ("\nIndex :",list [3]) #indexing
print ("\nSlice :",list [2:4])

#Tuple
print ("\n-------TUPLE-------")

Tup=(77,7.8,"Vasanth",[3,6,9],(4,5),{5:5,6:6},{8,5,2})
print (Tup)
print ("Index :",Tup[1]) # Indexing
print ("Index :",Tup[2][2]) # Indexing

print ("\n------Dictionary------")

Movie={
        "Name":"Uday",
        "Ph Num":9491143753,
        "Add":"Rjy",
        "Add":"Vjy"
        }
print (Movie)


print("\n------------SET------------")

set={11,22,33}
print ((set))



Uday="Vasudev"
print (Uday[4:4])

u=5
v=6
o=u+v
print (o)
