class uday:
    def vasudev(self):
        print("Yes This Is Uday")
    def Chinthalli(self):
        print("Idhi Naa Chinthalli")
    def add(self,a,b):
        self.a = a
        self.b = b
        c = a+b
        print("ADD :",self.a,self.b,c)
vasu = uday()
vasu.vasudev()
devi = uday()
devi.Chinthalli()
add = uday()
add.add(5,6)
add.add(9,9)

'''Using 'Class __inti__' Is A Constructor. in Constructor their is a self it is a default.
__init__ Method is a initialize a variables
'''
class mobile:
    uday = "Vasudev"
    vasu = "Under Vasudev"
    def __init__(self):
        print("I cant Here",mobile.vasu)
    def uday(self):
        print("I can Here",mobile.uday)
obj = mobile()
obj.uday()


class Bike_Rider:
    Rider = "Vasudev"
    def __init__(self,R_Name,R_Num,R_Bike,R_Chrg):
        self.R_Name = R_Name
        self.R_Num = R_Num
        self.R_Bike = R_Bike
        self.R_Chrg = R_Chrg
        print("Bike Owner :", Bike_Rider.Rider)
    def Rider_Details(self):
        print("Rider Details :",self.R_Name,self.R_Num,self.R_Bike,self.R_Chrg)
    def charg_pr_KM(self,KM):               # 10 to 50 = 10         50 to 70KM = 20
        if KM >= 0 and KM <= 50:
            Chrg = self.R_Chrg*10
            print("You Have To Pay :",Chrg)
        elif KM >=51 and KM <=70:
            Chrg = self.R_Chrg*20
            print("You Have To Pay :",Chrg)
        else:
            Chrg = self.R_Chrg*30
            print("You Have To Pay :",Chrg)

rider = Bike_Rider('Uday',949114753,'Apachi TVS',50)
rider.Rider_Details()
KM = int(input("Enter Your KM :"))
rider.charg_pr_KM(KM)
print()
print("---------@@@@@@----------")
print()
rider = Bike_Rider('Shilpa',8309964594,'Tvs_Jupiter',20)
rider.Rider_Details()
KM = int(input("Enter Your KM :"))
rider.charg_pr_KM(KM)

print("________Using For Loop And Keyworded Variable Length Agrument_______")

class Bike_Rider:
    Rider = "Vasudev"
    def __init__(self,R_Name,**Data):
        self.R_Name = R_Name
        self.Data = Data
        #self.R_Num = R_Num
        #self.R_Bike = R_Bike
        #self.R_Chrg = R_Chrg
        print("Bike Owner :", Bike_Rider.Rider)
        for j,k in Data.items():
            print(j,":",k)

    def Rider_Details(self):
        print("Rider Details :",self.R_Name)   #,self.R_Num,self.R_Bike,self.R_Chrg)
    def charg_pr_KM(self,KM):               # 10 to 50 = 10         50 to 70KM = 20
        if KM >= 0 and KM <= 50:
            Chrg = self.R_Chrg*10
            print("You Have To Pay :",Chrg)
        elif KM >=51 and KM <=70:
            Chrg = self.R_Chrg*20
            print("You Have To Pay :",Chrg)
        else:
            Chrg = self.R_Chrg*30
            print("You Have To Pay :",Chrg)

rider = Bike_Rider('Uday',R_Num = 949114753,R_Bike = 'Apachi TVS',R_Chrg = 50)
rider.Rider_Details()
KM = int(input("Enter Your KM :"))
rider.charg_pr_KM(KM)
print()
print("---------@@@@@@----------")
print()
rider = Bike_Rider('Shilpa',8309964594,'Tvs_Jupiter',20)
rider.Rider_Details()
KM = int(input("Enter Your KM :"))
rider.charg_pr_KM(KM)

+print("_____________Inheritance______________")

class A:
    def Uday(self):
        print("This Is Uday")

class B(A):
    def Swapna(self):
        print("This Is Swapna")

class C(B):
    def Gow(self):
        print("This is Gow")


a1 = A()
a1.Uday()
print()
print("_____________")
b1 = B()
b1.Uday()
b1.Swapna()
print("_____________")
print()
c1 = C()
c1.Uday()
c1.Swapna()
c1.Gow()





























