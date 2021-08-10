# Split string method
import random
names_string = input("Give me everybody's names, separated by a comma. ")
# This converts the string into a list, looks for ,space
#Created a list using "split on basis of ,"
names = names_string.split(", ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

#names is a list
print(names)
#print(names[0])

#Get the count in the list
Item_count = len(names)
#print(Item_count)

#randomly calculate the position 
#Item_count -1 to give us the idea about the length of the list
random_int = random.randint(0, Item_count - 1)
#Above output gives us the position
#print(random_int)

#Calling the certain position value in the list
names1 = names[random_int]
print( names1 + " is going to buy the meal today.")
#random_str = str(random_int)
#print("random_str")

#if random_int == names[0]:
 # print(f"{names[0]} is going to buy the meal today!")
#else:
  #print("No one is buying today!")

#x = names[0]

#print(x)

#second method

#print(random.choice(names))
#print(names2)


#if len(names) == names[0] :
 # print(f"{names[0]} is going to buy the meal today!")
#else :
 # print(f"{names[1]} is going to buy the meal today!")

#for 1 in list(Item_count) :
#print(Item_count[0])
#for i in range(Item_count):
 # print(random.choice(names))



