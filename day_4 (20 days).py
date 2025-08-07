n = int(input("Enter the value : "))
for i in range(1,n+1):
    if i==1 or i==n:
        str1=""
        for j in range(1,i+1):                               # 1
            str1+=str(j)+" "                                # 1 2
        print(" "*(n-i)+str1)                              # 1   3
    else:                                                 # 1     4
        str2=""                                          # 1 2 3 4 5
        for k in range(1,i+1):
            if k==1 or k==i:
                str2+=str(k)+" "
            else:
                str2+=" "+" "
        print(" "*(n-i)+str2)






def greet(arg1,arg2):
    print("Hello",arg1,"he is",arg2,"years old")
name = input("Enter the name : ")                     # Functions ( name argumanets )
age = int(input("Enter the age : "))                  # no order needed
greet(arg2=age,arg1=name)




def greet(name,age):
    print("Hello",name,"you are",age,"years old")
name = input("Enter the name : ")                         # order needed
age = int(input("Enter the age : "))
greet(age,name)



a = int(input("Enter the value : "))
b = int(input("Enter the value : "))
c = input("Enter Operator : ")

def add(a,b):
    print(a+b)
def sub(a,b):
    print(a-b)
def mul(a,b):
    print(a*b)
def div(a,b):                                                # Calculator
    print(a/b)

if c== "+":
    add(a,b)
elif c=="-":
    sub(a,b)
elif c=="*":
    mul(a,b)
else:
    div(a,b)


n = str(input("Enter the number : "))                      # str(input()) coz change the num into string to fing length
s= 0 
power = len(str(n))                              # ARMSTRONG NUMBER
for i in n:
    s+= int(i)**power               # int(i)  coz changed string in 1st line changing into intiger
if s==int(n):
    print("Number is Armstrong")
else:
    print("number is Not Armstrong")    



def is_prime(m):
    is_prime = True
    if m<= 1:
        is_prime = False
    else:
        for i in range(2,int(m**0.5)+1):
            if m%i==0:                               # user i/p number given => find prime numbers in range
                is_prime = False
                break
    if is_prime:
        print(m,"is prime ")
m = int(input("Enter the number : "))
for i in range(1,m+1):
    is_prime(i)



