'''
print("--------Simple Try-------")
a = 10
b = 20
try:
    c = a + b
    print("This is TRY Value :",c)
except:
    print("This is Exception")
print()
'''
#print("---------Final----------")
print("-------Exception Program Opened-------")
a = int(input("Enter The First Value :"))
b = int(input("Enter The Second Value :"))
try:
    c = a / b
    print("This is From Try [Block], Value Of A_B :",c)
except Exception as e:
    print("This is Exception (Exception as e)",e)
finally:
    print("______Exception Program Closed_______")











