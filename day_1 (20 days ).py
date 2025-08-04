# age  = int(input("Enter your age : "))
# if age >= 18:
#     print("You Can Vote")
#     if age >= 50:
#         print("Go to Ground floor")
#     else:
#         print("Go to first floor")
# else:
#     print("You Can't Vote")



# a = input()
# if a[0]==a[len(a)-1]:
#     print("Lucky")
# else:
#     print("Super Lucky")


# n = int(input("Enter the amount : "))
# if n == 10:
#     print("Collect Chips Packet")
# elif n ==20:
#     m = input("Select From the List [w,T,S,F,B] : ")
#     if m=="W":
#         print("Collect Water Bottle")
#     elif m=="T":
#         print("Collect Thumps Up")
#     elif m=="S":
#         print("Collect Sprite")
#     elif m=="F":
#         print("Collect Fanta")
#     elif m=="B":
#         print("Collect Bindu")
#     else:
#         print("Product Not Exist")
# else:
#     print("No Products Available,Order Declined")
# print("Thanks For Visiting, See you Soon")


# a = input()
# if a==a[ :: -1]:
#     print("palindrome")
# else:                                   # Palindrome using if condition
#     print("not")




# a = input("Enter the word : ")
# for i in range(0,1):                       #palindrom using loops
#     if a==a[ :: -1]:
#         print("Word is Palindrome")
#     else:
#         print("Word is not Palindrome") 



# a = input("Enter the word : ")

# r_str = " "
# for i in a:
#     r_str = i+r_str
# print(r_str)

                                             # Reversing input


# n = input("Enter the word : ")

# r_str =" "
# for i in range(len(n)-1, -1, -1):
#     r_str += n[i]
# print("palindrome"if r_str == n  else "not palindrome")


# num = int(input("Enter a number: "))
# original = num
# reverse = 0

# while num > 0:
#     digit = num % 10         # Get last digit
#     reverse = reverse * 10 + digit  # Add digit to reverse
#     num = num // 10          # Remove last digit

# # Compare original and reverse
# if original == reverse:
#     print("It is a palindrome number.")
# else:
#     print("It is not a palindrome number.")



# n=input()
# is_palindrome = True
# i=0
# j=len(n)-1
# while(i<=j):
#     if n[i]==n[j]:
#         i+=1
#         j-=1                                                   # palindrome using While loop
#     else:
#         is_palindrome = False
#         break
# print("palindrome" if is_palindrome else "not palindrome")



# n = int(input("Enter the number : "))
# is_prime = True
# for i in range(2,n):
#     if n%i==0:
#         is_prime = False
# print("is a prime number" if is_prime else "is not a prime number")



print(3*(2+1))