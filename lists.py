#lists are the most common type of data structure in python
#Dictionary is the second most
a_list = [0,13,95,34,56,12]
print(a_list[0])
print(a_list[5])
print(a_list[-1])
print(a_list[0:3])
print(a_list[1:3])
print(a_list[-3:-1])
print(a_list[-3:])
print(a_list[:])
print(a_list)
print(a_list[0::2]) #Grabs every other number
print(a_list[1::2])
print(a_list[::-1]) #Reverses list

b_list = list(reversed(a_list))
print(b_list)
a_list.reverse()
print(a_list)

a_list.sort()
print(a_list)
print(sorted(a_list)) #Doesn't change the original list

a_list.append(7) #When it is itemname.function, it means you are changing the item
#You can only add a single value with append
print(a_list)
a_list.extend([53,27]) #Extend lets you add multiple values
print(a_list)

a_list.pop() #Pop removes one thing off of the end of the list
print(a_list)

a_list.remove(95) #Removes a specific object 95 from a list
print(a_list)

del a_list[3] #Deleted the third item in the list
print(a_list)

a_list = a_list[0:3] #Removes all but the first three elements
print(a_list)

a_list.insert(0,3) #insert 3 at location 0
print(a_list)

a_list.insert(2,3)
print(a_list)



