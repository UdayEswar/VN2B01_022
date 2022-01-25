print("---Using Built in fun---")
strg = "Uday"
print("Lng of String :",len(strg))
print()

print("___Using Algorithm without fun___")

str1 = "Vasudev"
ln = 0
for i in str1:
    ln = ln + 1
print("Algo Lngth :",ln)
print()

print("___Algo With Fun___")

def find_lng(uday="123456"):
    ln = 0
    for i in uday:
        ln = ln + 1
    return ln
print("len With Fun :",find_lng("123"))  # User defined Function
u_ln = find_lng()
print("Main Fun :",u_ln)  # Main Function

str1 = str1 + 'Add'
print("Full Ln Of String :",len(str1))
# Here the state variable str1 can be accessed and modified by anyone in entire project
# Solution is , combine both state and behavior and configure in a single entity(i.e, class)
print()

print("+++Without OOPS+++")
# state
car_name = "Toyota"
car_model = "MK57"
Car_price = "700000"
# Behavior
def get_Cdetails(name,model,price):
    print("Car Details :",name,"-",model,"-",price)
get_Cdetails(car_name,car_model,Car_price)
print()


print("___With OOPs___")
class Car_Details:

    def __init__(self,name,model,price):
        self.name = name
        self.model = model
        self.price = price
     # Behavior
    def car_details(self):
        print("Car Details :",self.name,"-",self.model,"-",self.price)
# Objection Creation
uday = Car_Details('Ford','Ak47',1000000)
uday.car_details()

print("----Insta Method----")

class Bike_race:
    def __init__(self,Name,ph_num):
        self.Name = Name
        self.ph_num = ph_num

    # Insta Method
    def get_race(self):
        print("Rider Details :",self.Name,self.ph_num)

    def Charges(self,Charges):
        print("Extra Charges For Extra Ride :", Charges)
        if Charges > 50 and Charges<=60:
            a = Distance*10
            print("You Have To Pay :",a)
        elif Charges >=61 and Charges<=70:
            b = Distance*20
            print("You Have To Pay :",b)
        elif Charges>=71 and Charges<=80:
            c = Distance*30
            print("You Have To Pay :",c)
        else:
            Charges>81
            d = Distance*50
            print("You Have To Pay :",d)

Ride = Bike_race("Uday",9491143753)
Bike_race.get_race(Ride)
Distance = int(input('Enter Your Ride Km :',))
Bike_race.Charges(Ride,Distance)

Ride.get_race()
Ride.Charges(Distance)














