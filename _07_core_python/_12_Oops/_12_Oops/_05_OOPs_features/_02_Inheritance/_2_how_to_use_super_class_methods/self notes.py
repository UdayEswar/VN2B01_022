# single inh

print("++++++single inh++++++")
print()
class parent:
    def Swapna(self):
        print("This is Parent Class")
class Child(parent):
    def Gow(self):
        print("This is Child Class")
obj = Child()
obj.Gow()
obj.Swapna()


# Multi Level inh
print('+++++Multi Level inh+++++')
print()

class parent:
    def Swapna(self):
        print("This is Parent Class")
class Child(parent):
    def Gow(self):
        print("This is Child Class")
class ChinnaChild(Child):
    def Simha(self):
        print("This is ChinnaChild Class")

obj = ChinnaChild()
obj.Simha() # This Is Won Function
obj.Gow() # This is Child Function
obj.Swapna() # This is parent Function

# Hierarchical inheritance (It means one parental class and two Child Class)
print("=======Hierarchical inh=======")
print()
class vn2:
    def uday(self):
        print("Vasudev")
class vn22(vn2):
    def gow(self):
        print("Uday")
class vn222(vn2):
    def Swap(self):
        print("Vasu")
obj = vn222()
obj.Swap()
obj.uday()

# Multiple inh
print("------Multiple inh------")
print()
class parent:
    def simha(self):
        print("This is parent")
class son:
    def basi(self):
        print("This is son")
class small_son(parent,son):
    def uday(self):
        print("This is small son")
obj = small_son()
obj.uday()
obj.basi()
obj.simha()


# Super inh
print("------Super inh-------")
print()
class A:
    def __init__(self):
        print("This is A")
    def uday(self):
        print("Vasudevs Nature Talk")
class B(A):
    def __init__(self):
        super().__init__()
        print("This is B")
    def vasu(self):
        print("Vasudaika Kutumbam")
obj = B()          # Because of init We are Getting this function out put
obj.vasu()
obj.uday()




