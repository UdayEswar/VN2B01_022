
a=int(input("Enter The Your Salary :"))
b=int(input("Enter Your Service in Years :"))
if b>10:
    c=a*0.1
    print("Bonus amount for salary",c)
    print("Total salary with Bonus",c+a)
elif b<=10 and b>=6:
    d=a*0.08
    print("Bonus amount for salary",d)
    print("Total salary with Bonus",d+a)
else:
    e=a*0.05
    print("Bonus amount for salary",e)
    print("Total salary with Bonus",e+a)


