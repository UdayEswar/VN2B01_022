'''
# STATE
em_name = "Uday"
em_Num = 9491143753
em_Sal = 50000
# BEHAVIOR
def em_details(em_name,em_Num,em_Sal):
    print("Em_Details :",em_name,em_Num,em_Sal)

em_details(em_name,em_Sal,em_Num)

# BEHAVIOR
def em_details():
    print("Em_Details :",em_name,em_Num,em_Sal)

em_details()
print("+++++++Using Oops+++++++")
class Mobile:
    def __init__(self,mobile,color,price):
        self.mobile = mobile
        self.color = color
        self.price = price

    def get_M_Info(Details):
        print("Mobile details :",Details.mobile,Details.color,Details.price)
mobile = Mobile("Redmi k 20 pro","Blue",32000)
mobile.get_M_Info()


class Computer:

    def __init__(self,):
        print("i7","8gb","1TB HDD")

comp1 = Computer()
Computer.config(comp1)



def get_sum(num1, num2):
    result = num1 + num2
    return result

    print("Sum of 2 numbers is : ", get_sum(num1, num2))

get_sum(4,5)


a = 5
b = 6
c = 7
def Sum(f,d,e):
    g= 5
    print(f+d+e+g)

Sum(7,9,10)
'''

'''
# Key Words
def person(name,age,Num):
    print(name)
    print(age)
    print(Num)
person(Num= 6666, age=28,name="uday")

# Default
def person(name = "Vasudev",age=25):
    print(name,age)
person("Uday",23)
person()

# Variable Length Argument
def sum(a,*b):
    print(a)
    print(b)
sum(5,5,6,6)

print("_______")

def sum(a,*b):
    c = a
    m = 0
    for i in b:
        m = m + i
        print(m)
    print("ddss",c)
    #print(d)
    #print(c)
    #print(a)
    #print(b)
sum(5,10,10,20)
'''
def uday(*a):
    b = 0
    for i in a:
        b = b + i
        print(b)

uday(1,2,3,4,5)


def uday(kk,ll,gg):

class Uday:
    def vasu(self,chg,jj ):
        self.chg = chg








