'''

def uday(a,b):
    return a*b
c=uday(5,5)
print(c)

def uday(a):
    return a*5
print(uday(3))


def fun (n):
    return lambda a:a+n
a=5
c=fun(2)
print(c(10))

def add (x,y):
    c=x+y
    print(c)

def Sub (x,y):
    d=x-y
    print(d)

add(55,55)
add(99,99)

Sub(6,5)


def add_sub(x,y):
    a = x+y
    b = x-y
    return a,b
result1,result2=add_sub(5,6)


print(result1,result2)

def sum ():
    print("uday")
sum()'''

def sun():

    for k in range(20,50):
        if k % 5==0:
            print("This Is Modular With 5 :",k)

sun()





