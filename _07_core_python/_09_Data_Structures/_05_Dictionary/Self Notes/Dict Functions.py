print("+++Dict Functions+++")
print("Length :-")
Data = {
        "Name" : "Uday",
        "Work" : "Software Engg",
        "Ph_Num":  9491143753,
        "Sal"   : "100,000"
}
print("Length Of Dict :",len(Data))
print("Type :-")
print("Type Of Dist :",type(Data))
print()
print("Dict ==> Str :-")
print("Before :",type(Data))
Ch_Str = str(Data)
print("After :",type(Ch_Str))
print()

print("----Built-in-Functions----")
Dict = {
        "Company" : "Vn2 Solutions",
        "Name"    : "Uday",
        "Mobile"  :  9491143753,
        "E_id"    : "VN2-BO_022",
        "Address" : {"Village" : "Daravaram", "Dr_No" : "1-99/2"}
       }
print("===Key===")
a = Dict.keys()
print("Keys :",a,type(a))
a = list(Dict.keys())
print()
print("List of Dict Keys :")
for key in Dict.keys():
    print(key)
print()
print("===Values===")
b = Dict.values()
for val in b:
    print("Data Values :",val,type(b))
print("List of Data :",list(b))
print()
print("")
for key in Dict.values():
    print(key)
print()
print("===Items===")
items = Dict.items()
for i in items:
    print(i)
print()
print("Fromkeys :-")
dic = {1:2,1:3}
dic = dic.fromkeys([10,20,30],"Uday")
dic
print(dic)
print()

print(".Copy")
a={2:0,3:0,4:0}
b=a.copy()
print("Before :",a)
print("After :",b)
print()

'''
print(".Has_key")
DIC = {1:2,5:5,"Uday":"Vasudev"}
print(DIC)
print("Has_key :",DIC.has_key("Uday"))
'''
print("---.Get---")
print(Dict)
print(Dict.get('Company'))



