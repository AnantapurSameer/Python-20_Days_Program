# list_1 = [3,6,4,5,6,3]
# first_sum = sum(list_1)
# second_sum = sum(set(list_1))*2
# res = second_sum-first_sum
# print(res)



# n = int(input("Enter the number : "))
# fact = 1
# for i in range(n,1,-1):                              # Factorial
#     fact *= i
# print(fact)



# n = 5
# f = 0
# for i in range(1,11):             # Sum of 1st 10 factorials of input
#     f = n*i+f
# print(f)    



# n = int(input("Enter number : "))
# for i in range(1,11):                       # Tables
#     print(n,"x",i,"=",n*i)



# list_1 = [1,7,9,7,4,6,2]
# target = 7
# for i in range(len(list_1)):               # Linear search
#     if target == list_1[i]:
#         print(i)
#         break




# list_1 = [1,2,3,4,5,6,7,8,9,10]
# target = int(input("Enter the target : "))
# start = 0
# end = len(list_1)-1
# index = -1
# while(start<=end):
#     middle = (start+end)//2
#     if list_1[middle]==target:
#         index = (middle)
#         break
#     elif list_1[middle]>target:
#         end = middle - 1
#     else:
#         start = middle+1
# if index != -1:
#     print(index)
# else:
#     print("Not found")



# n = int(input("Enter no of stars : "))
# for i in range(1,n+1):                              # Stars pattern
#     print("* "*i)




# n = int(input("Enter no of stars : "))
# for i in range(n,0,-1):                              # inverted Stars pattern
#     print("* "*i)




# n = int(input("Enter no of stars : "))                 # 1
# for i in range(1,n+1,):                                # 1 2           
#     for m in range(1,i+1):                             # 1 2 3
#         print(m,end = " ")                             # 1 2 3 4 
#     print()
  



# n = int(input("Enter the numbers : "))
# for i in range(n,0,-1):                                      # inverted numbers triangle
#     for j in range(i,0,-1):
#         print(j,end=" ")
#     print()    




# n = int(input("Enter the value : "))
# for i in range(1,n+1):
#     for j in range(1,n-i+1):
#         print(" ",end=" ")
#     for h in range (1,2*i):                                    # Piramid
#         print("*",end=" ")
#     print()






# n = int(input("Enter the value : "))
# for i in range(1,n+1):                                       # (n-i) = For spaces   [pyramid]
#     print(" "*(n-i)+"* "*i)




# n = int(input("Enter the value : "))
# for i in range(n,0,-1):                                     # Inverted Pyramid
#     print(" "*(n-i)+"* "*i)




# n = int(input("Enter the value : "))
# for i in range(1,n+1):
#     for j in range(1,i+1):
#         print(" "*(n-i),j,end=" ")
#     print()





# n = int(input("Enter the value : "))
# for i in range(1,n+1):
#     if i==1 or i==n:
#         print("* "*i)                              # Hollow Triangle
#     else:
#         print("*"+" "*(2*i-3)+"*")
   




# n = int(input("Enter the value : "))
# for i in range(1,n+1):
#     for j in range(n-i):
#         print(" ",end=" ")                        # hollow Piramid
#     for h in range (1,2*i):        
#         if h==1 or h== 2*i-1 or i==n:                           
#             print("*",end=" ")
#         else:
#             print(" ",end=" ")
#     print()
                      
