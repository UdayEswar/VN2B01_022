class animal:
    def _init_(self,cat,dog,duck):

        self.cat=cat
        self.dog=dog
        self.duck=duck

    def eating(self):
        print("super class is created",self.cat,self.dog,self.duck)

#obj=animal('cow','buffellow','cds')
#obj.eating()

class cruel_animals:                    # A
    def _init_(self,cheethah,jaguar,lion):
        #super()._init_()
        self.cheethah=cheethah
        self.jaguar=jaguar
        self.lion=lion
    def eating2(self):
        print("these are cruel animals :",self.cheethah,self.jaguar,self.lion)

#obj1=cruel_animals("cheethah","jaguar","lion")
#obj.eating()

class sea_animals(animal,cruel_animals):            # B
    def _init_(self,penguin,fish,dolphin,seal):
        animal._init_(self,"cheethah,jaguar,lion")
        cruel_animals._init_(self,"cheethah,jaguar,lion")
        sea_animals._init_(self,"penguin,fish,dolphin,seal")
        self.penguin=penguin
        self.fish=fish
        self.dolphin=dolphin
        self.seal=seal
    def sanimals(self):
        print("these are sea animals :",self.penguin,self.fish,self.dolphin,self.seal)


obj2=sea_animals()
obj2.sanimals()
obj2.eating()
obj2.eating2()
#obj.sanimals()








'''
class T_animals(cruel_animals,sea_animals):
    def Gow(self):
        print("total animals :")
obj = T_animals(cruel_animals,sea_animals,)
obj.eating()
obj.sanimals()
'''



class animal:
    def _init_(self,cat,dog,duck):

        self.cat=cat
        self.dog=dog
        self.duck=duck

    def eating(self):
        print("super class is created",self.cat,self.dog,self.duck)

#obj=animal('cow','buffellow','cds')
#obj.eating()

class cruel_animals:                    # A
    def _init_(self,cheethah,jaguar,lion):
        #super()._init_()
        self.cheethah=cheethah
        self.jaguar=jaguar
        self.lion=lion
    def eating2(self):
        print("these are cruel animals :",self.cheethah,self.jaguar,self.lion)

#obj1=cruel_animals("cheethah","jaguar","lion")
#obj.eating()

class sea_animals(animal,cruel_animals):            # B
    def _init_(self,penguin,fish,dolphin,seal):
        animal._init_(self,"cheethah,jaguar,lion")
        cruel_animals._init_(self,"cheethah,jaguar,lion")
        sea_animals._init_(self,"penguin,fish,dolphin,seal")
        self.penguin=penguin
        self.fish=fish
        self.dolphin=dolphin
        self.seal=seal
    def sanimals(self):
        print("these are sea animals :",self.penguin,self.fish,self.dolphin,self.seal)


obj2=sea_animals()
obj2.sanimals()
obj2.eating()
obj2.eating2()
#obj.sanimals()








'''
class T_animals(cruel_animals,sea_animals):
    def Gow(self):
        print("total animals :")
obj = T_animals(cruel_animals,sea_animals,)
obj.eating()
obj.sanimals()
'''




class animal:
    def _init_(self,cat,dog,duck):

        self.cat=cat
        self.dog=dog
        self.duck=duck

    def eating(self):
        print("super class is created",self.cat,self.dog,self.duck)

#obj=animal('cow','buffellow','cds')
#obj.eating()

class cruel_animals:                    # A
    def _init_(self,cheethah,jaguar,lion):
        #super()._init_()
        self.cheethah=cheethah
        self.jaguar=jaguar
        self.lion=lion
    def eating2(self):
        print("these are cruel animals :",self.cheethah,self.jaguar,self.lion)

#obj1=cruel_animals("cheethah","jaguar","lion")
#obj.eating()

class sea_animals(animal,cruel_animals):            # B
    def _init_(self,penguin,fish,dolphin,seal):
        animal._init_(self,"cheethah,jaguar,lion")
        cruel_animals._init_(self,"cheethah,jaguar,lion")
        sea_animals._init_(self,"penguin,fish,dolphin,seal")
        self.penguin=penguin
        self.fish=fish
        self.dolphin=dolphin
        self.seal=seal
    def sanimals(self):
        print("these are sea animals :",self.penguin,self.fish,self.dolphin,self.seal)


obj2=sea_animals()
obj2.sanimals()
obj2.eating()
obj2.eating2()
#obj.sanimals()








'''
class T_animals(cruel_animals,sea_animals):
    def Gow(self):
        print("total animals :")
obj = T_animals(cruel_animals,sea_animals,)
obj.eating()
obj.sanimals()
'''




class animal:
    def _init_(self,cat,dog,duck):

        self.cat=cat
        self.dog=dog
        self.duck=duck

    def eating(self):
        print("super class is created",self.cat,self.dog,self.duck)

#obj=animal('cow','buffellow','cds')
#obj.eating()

class cruel_animals:                    # A
    def _init_(self,cheethah,jaguar,lion):
        #super()._init_()
        self.cheethah=cheethah
        self.jaguar=jaguar
        self.lion=lion
    def eating2(self):
        print("these are cruel animals :",self.cheethah,self.jaguar,self.lion)

#obj1=cruel_animals("cheethah","jaguar","lion")
#obj.eating()

class sea_animals(animal,cruel_animals):            # B
    def _init_(self,penguin,fish,dolphin,seal):
        animal._init_(self,"cheethah,jaguar,lion")
        cruel_animals._init_(self,"cheethah,jaguar,lion")
        sea_animals._init_(self,"penguin,fish,dolphin,seal")
        self.penguin=penguin
        self.fish=fish
        self.dolphin=dolphin
        self.seal=seal
    def sanimals(self):
        print("these are sea animals :",self.penguin,self.fish,self.dolphin,self.seal)


obj2=sea_animals()
obj2.sanimals()
obj2.eating()
obj2.eating2()
#obj.sanimals()








'''
class T_animals(cruel_animals,sea_animals):
    def Gow(self):
        print("total animals :")
obj = T_animals(cruel_animals,sea_animals,)
obj.eating()
obj.sanimals()
'''