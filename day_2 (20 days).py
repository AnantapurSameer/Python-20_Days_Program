name = "all silver tea cups.".title()
print(name)                                             # capitalize 1st letter of words in sentence




num = "1 2 3 4"
num_list=num.split()                                      # splitting
print(num_list)



num = "1 2 3 4"
num_list=num.split(" ")                                      # splitting space include
print(num_list)



name = "pyhton is a programming language"
name_list=name.split("a")                                      # remove "a" from the sentance
print(name_list)




list_a = ['pyhton is ', ' progr', 'mming l', 'ngu', 'ge']
string_a = "a".join(list_a)                                       # join ( joinr the give input)
print(string_a)




name = "all silver tea cups.".title()
name_list = name.split(" ")
string_a = "".join(name_list)
print(string_a)





name = "all silver tea cups."
name_list = name.split(" ")
string_a = "_".join(name_list)
print(string_a)


name = "all silver tea cups.".title()
name_list = name.split(" ")
string_a = "-".join(name_list)
print(string_a)



name = "all silver tea cups.".title()
str1 = name[0].lower()+name[1:]
sam = str1.split(" ")
string_a = "".join(sam)
print(string_a)




n = input("Enter the word : ").lower()
c=0
for i in n:
    if i in "aeiou":                           # count vowels in input
        c+=1
print(c)




n = input("Enter the word : ").lower()
c=0
for i in n:
    if i not in "aeiou":                           # count consonents in input
        c+=1
print(c)




li = [2,1]
li.sort()
print(li)



list = input("Enter the nums : ").split()                   # Sorted() using
list2 = sorted(list)
print(list)



li = list(map(int,input("Enter the numbers : " ).split()))               # sorting using ( map )
li.sort()
print(li)




list_1 = [3,2,5,8,3,9,10,999]
highest = list_1[0]
for i in range(len(list_1)):
    if list_1[i]>highest:                                               # highest number
        highest = list_1[i]
print(highest)




list_1 = [3,2,5,8,3,9,10,999]
highest = list_1[0]
for i in range(len(list_1)):
    if list_1[i]>highest:                                               # highest and second highest number
        highest = list_1[i]
second  = list_1[0]
for i in range(len(list_1)):
    if list_1[i]>second and highest>list_1[i]:                                             
        second = list_1[i]
print(second)