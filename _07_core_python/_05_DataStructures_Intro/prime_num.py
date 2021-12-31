number=int(input("Enter a number" ))
if number%2==0 or number%3==0 or number%5==0 or number%7==0 :
    if number%2==0 and number%3==0 :
        print("it is a not a prime number")
    elif number%5==0 and number%7==0 :
        print("it is not a prime number")
    else :
        print(("it is a prime number"))
else :
    print("it is a prime number")
