def add(x,y):
    return(x+y)
a = int(input("Enter 1st number : "))                       #Return
b = int(input("Enter 2nd number : "))
c = add(a,b)
print(c)


def greet(arg_1="Hi",arg_2="Sameer"):
    print(arg_1+" "+arg_2)
greeting = input()
name = input()
greet(arg_2=name)



i = list(map(int,input().split()))             # list input storing in int using map
print(i)                                       # i/p :- 2 3 4 5 6 => [2,3,4,5,6]



def fact(n):
    if n <= 0:
        return 1
    return n*fact(n-1)                        # factorial using Recurssion

n = int(input("Enter the number : "))
print(fact(n))



def sum(n):
    if n <= 1:
        return 1
    return n+sum(n-1)                        # Sum of 1st 10 natural numbers using Recurssion

n = int(input("Enter the number : "))
print(sum(n))




def fibb(n):
    if n<= 0:
        return 0
    if n==1:                                   # Fibonacci series usingRecurssion
        return 1
    return fibb(n-1) + fibb(n-2)

n = int(input("Enter the number : "))
for i in range(n):
    print(fibb(i),end=" ")



'''   \\\\\\\\\\\\\//////////////[ OOPS ]\\\\\\\\\\\\\\\/////////////         '''



class Iphone:
    def icloud(self):
        print("free 5gb space")

    def call(self,number):
        print("calling.....",number)
iphone16pro = Iphone()         # obj creation

number1 = int(input("Enter number : "))
print(type(iphone16pro))
iphone16pro.call(number1)



class AmezonService:
    def __init__(self,agentname,agentId,customerid):
        self.customerid = customerid
        self.agentname = agentname
        self.agentid = agentId
agentname="sai"
agentid=1
complaint=input("Enter your name : ")
customerid=int("Enter yout issue : ")
