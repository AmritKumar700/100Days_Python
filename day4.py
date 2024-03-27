#In this program I am using random module and importing random 
#using this random we can specify a specific range for generating random 
#numbers in between the range this could be done by using a varialble and
#storing this code in that liek "x = random.randint(1,10)"
#When we print(x) we will get each time a random numbers between 1 and 10 including 1 and 10

# import random 

# random_integer = random.randint(1,10)
# print(random_integer)

# love = random.randint(1,100)
# print(f"Your love score is {love}.")

#.........................LEARNING LIST....................
#use square bracket for storing and printing elements ib lists
list1 = ["Amrit","Ritika","Puchu","Ritu"]
print(list1[2])
#start counting from 0,1,2,3,..........................,n
#if you print([-1]) it will give Ritu count from last
#...................................................Changing Elements in the lists..
list1[0]="Amritika"
print(list1[0])#Amrit has been changed to Amritika
#...................................................Printing Whole List.............
print(list1)
#print(list1) will print ['Amritika', 'Ritika', 'Puchu', 'Ritu'] whole list

#.................................Adding Items to the list1............
#adding at last 
list1.append("AmritPuchu")#this will add AmritPuchu at last of the list1
print(list1)
#we can do lot more things in the list like pop,remove,inster etc in the list
#list1.extend("EFG")
print(list1)
list1.insert(3,"Aka")
print(list1)
#.............................Nested Lists...........
###Suppose we have two list already then we can add these lists into another example
list0 = ["a","e","i","o","u"]
list2 = ["l","i","s","t"]
Nested_list = [list0 , list2] #Don't put list0 & list2 in " " in this otherwise it will count it as items
print(Nested_list)#Output will be [['a', 'e', 'i', 'o', 'u'], ['l', 'i', 's', 't']]
