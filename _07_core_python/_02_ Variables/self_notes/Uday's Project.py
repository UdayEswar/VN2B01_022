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

Uday,Vasu,Vasudev=44,55.5,'Vassunitha'
print (Uday,Vasu,Vasudev)
print (id(Vasudev),id(Uday),id(Vasu))
print (type(Uday),type(Vasu),type(Vasudev))


c=45
d=c+5
print (d)


'''Here Deleting B Value'''
B=143
print (B)
del (B)

print (B)