print("\t\t------Dictionary------")
Dict = {
        "Company" : "Vn2 Solutions",
        "Name"    : "Uday",
        "Mobile"  :  9491143753,
        "E_id"    : "VN2-BO_022",
        "Address" : {"Village" : "Daravaram", "Dr_No" : "1-99/2"}
       }
for key,val in Dict.items():
    print(key,":", val)
print("Village Name :",Dict["Address"]["Village"])
print("Dr_No :",Dict["Address"]["Dr_No"])
print()
# Keys Are Immutable And Values are Anything.
Dict = {
            100 : 22,
            200 : 33,
            True : "Uday",
            False : "Nothing",
            "HI" : "Okay",
            True : True,
            (1,2,3) : (4,5,6),
            (1,2,3) : (4,5,6), #Duplicate
            (2,3,1) : (4,5,6)
}

for Uday in Dict:
    print(Uday)
for key,value in Dict.items():
    print(key,":",value)
print("In Dictionary Keys Must Be Unique (We Can Use Tuple As A Key) Values Can Be Anything")
print()
print("---Dictionary Is Mutable---")

print('Creating :-')
Data = {
        1 : "One",
        2 : "Two",
        True : False,
        "Uday" : True
        }
for i in Data:
    print("Key :",i)
print()

print("Retrieve :-")

print("Dict Type :",type(Data))
print("Dict Item :",Data["Uday"])
print()

print("Update :-")

Data[2] = "Devi"
Data["Uday"] = [143]
print("Updated :",Data)
print()

print("Delete :-")
del Data[True]
del Data["Uday"]
print(Data)

Data.clear()
print("Cleared :",Data)









