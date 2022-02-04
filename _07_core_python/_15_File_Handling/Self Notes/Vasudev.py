print("---Welcome To 'VASUDEVS' Program---")
print("\t\t@___HI Everyone___@")
print("Here You Can Download Some Img's And You Can Do Ar-thematic Operations Also.")
print("Here Choose What You Want To Do.! Ex: Ar =>'Arth', Md =>'Media'")
print("")

try:
    x = input("Enter 'Ar Or Md :")
    if x == "Ar" or x == "ar":
        print("Here You Can Choose All Types of Ar_thematic Operations")
        print("+,-,*,/")
        a = int(input("Enter Number :"))
        b = int(input("Enter Another Number :"))
        print("This is Add = ",a+b,"\nThis is Sub = ",a-b,"\nThis is Multiply = ",a*b,"\nThis is Division = ",a/b)

    #elif x == "Md" or x == "md":
     #   print("Here You Can Choose All Types Of Media")

    else:
        print("v")

except:
    print("Invalid Entry")
'''
x = input("Enter Uday :")
if x == "Ar" or x == "ar":
    print("Ar")
'''


