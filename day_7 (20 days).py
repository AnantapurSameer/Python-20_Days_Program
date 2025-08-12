# num = [1,4,6,5,3]
# target = int(input("Enter the target number : "))
# res = "-1"
# flag = False                                  # find which 2 nums sum is equal to target
# for i in range(len(num)-1):
#     for j in range(i+1,len(num)):
#         if num[i]+num[j] == target:
#             res = num[i],num[j]
#             break
# print(res)



# num = [1,6,4,5,3]
# target = 7
# unique = set()                                       # set of 2 numbers which sum if equal to target
# for i in num:
#     required = target - i
#     if required in unique:
#         print(i,required)
#     unique.add(i)




# num = [1,2,3,5]
# for i in range(len(num)):                      # finding missing number
#     if num[i]+1 != num[i+1]:
#         print(num[i]+1)
#         break



# l = [1,2,3,4,5]
# k = int(input("Enter no.of times rotation : "))                          # List Rotation = [1,2,3,4,5]
# rotation = k%len(l)                                                      # k = 3 => [3,4,5,1,2]
# print(l[-rotation:]+l[:-rotation]) 






