#Single level

class Parent:

    def __init__(self,name,age):
        self.name = name
        self.age = age
    
    def greet(self):
        print("Hello")

class Child(Parent):

    def sound(self):
        print(f"I'm {self.name}")



hierarchical

class Child2(Parent):

    def sound(self):
        print("hierarchical inheritence")
    
    def car(self):
        print("I'm having lambo")


#Multiple, multi-level

class Grandchild(Child,Child2):

    def sound(self):
        print(f"I'm {self.name}, implementing multi level inheritence")

c1 = Grandchild("rahul",1)
c1.sound()




#Encapsulation

class Bank:

    def __init__(self,acc,balance):
        self.acc = acc
        self.__balance = balance
        print("account created successfully")

    def get_balance(self):
        print(self.__balance)

    def set_balance(self,amount):
        self.__balance +=amount

kotak = Bank("saving",1000)
kotak.set_balance(2000)
kotak.get_balance()
    
    
c3 = Child("ram",21)
c4 = Child2("hari",20)
c3.sound()
c4.sound()




#Method over loading

def add(a=0,b=0,c=0):
    print(a+b+c)


add(1,2)



#Abstration

from abc import ABC,abstractmethod

class Car(ABC):

    @abstractmethod
    def b(self):
        pass

class BMW(Car):

    def b(self):
        print("breaks applied")

car1 = BMW()
car1.b()
      



class ranga:

    def __init__(self,name,age):
        self.name = name
        self.age = age
    
    def greet(self):
        print("Hello")

class sreenu(ranga):

    def sound(self):
        print(f"I'm {self.name},my age{self.age}")
class rakhi(sreenu):
    def reddy(self):
        print("rakhi is watchimg..")




c1=rakhi('rakhi',21)
c1.reddy()