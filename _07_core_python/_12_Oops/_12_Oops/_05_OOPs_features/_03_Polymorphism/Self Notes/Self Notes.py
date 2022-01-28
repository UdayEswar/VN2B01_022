print(",,,,...Polymorphism...,,,,")
print("          ;;;;;               ")
# Method Overloading
# Same class
# Same Function or method Name
# Different Parameters
print("......Method Overloading......")

class A:
    def sum(self, a, b):    # This is normal
        return a + b
    def s(self, a, b, c = 6):     # This is Overloading because of Given Perameters
        return a + b + c
obj = A()
print(obj.sum(5,6))
print()
print("////...Method Over-Riding...////")
# method Over-riding
# Different Classes
# Same methods names
# Different Perameters
class A:
    def vasu(self):
        print("This is A")
class B(A):
    def uday(self):
        print("This is B")
        super().vasu()
class C(B):
    def gow(self):
        print("This is C")
        super().uday()
class D(C):
    def uday(self):
        print("This is D")
        super().gow()
obj = D()
obj.uday()



