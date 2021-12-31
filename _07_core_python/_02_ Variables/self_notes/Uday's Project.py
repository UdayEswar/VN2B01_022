'''
Here I'm Discussing About int, float, Complex, bool, variables Memory Address,
'''

x=10
print (type(x),x)
print (id(x))

X=1.2
print (type(X),X)
print (id(X))

y=1+1j
print (type(y),y)
print (id(y))

Y=True
print (type(Y),Y)
print (id(Y))

print (x,X,y,Y)

_x=44
print (id(_x),type(_x),_x)

_X=44+55+66
print (_X)

Uday,Vasu,Vasudev=44,55.5,"Vassunitha"
print (Uday,Vasu,Vasudev)
print (id(Vasudev),id(Uday),id(Vasu))
print (type(Uday),type(Vasu),type(Vasudev))


c=45
d=c+5
print (d)


'''Operators'''

a=45
b=5
c=a+b
print(c)

print (5+5)

f=20
g=25
if f==g:
    print ("f==b is True")
else:
    print ("false")

v=20
b=30
if v<b:
    print ("True")
else :
    print ("false")



t=88
p=99
print ((t+p),(t-p),(t*p),(t/p),)
print (id(t+p),id(t-p),id(t*p),id(t/p))
print (id(t),id(p))

a=20
b=30
if a>b:
    print ("Uday")
elif a<b:
    print ("Vasudev")
else:
    print ("swetha")


a=1
b=1
if a>b:
    print ("Vasu")
elif a<b:
    print ("Uday")
else :
    print ("Simha")
