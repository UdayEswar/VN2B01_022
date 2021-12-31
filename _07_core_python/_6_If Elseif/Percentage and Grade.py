a=int(input("Enter The Percentage :"))
if a<=100 and a>80:
    print ("A")
elif a<=80 and a>60:
    print ("B")
elif a<=60 and a>45:
    print ("C")
elif a<=45 and a>=35:
    print ("D")
elif a<=34 and a>=0:
    print ("Fired")
else:
    print("Invalid entry")