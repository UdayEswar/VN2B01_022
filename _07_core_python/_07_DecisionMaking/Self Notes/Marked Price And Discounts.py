a=int(input("Enter The price :"))
if a>10000:
    b=a*.2
    print("The Discount Price is :",b)
    print("After Discount :",a-b)
elif a<=10000 and a>7000:
    c=a*.15
    print("The Discount Price is :",c)
    print("After Discount :", a-c)
else :
    d=a*.1
    print("The Discount Price is :",d)
    print("After Discount :",a-d)









