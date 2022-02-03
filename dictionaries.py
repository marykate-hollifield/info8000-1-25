a_dict = {"k1":5,"k2":7,1:"hello"} #Curly braces are used for dictionaries and sets #key is in quotes and value is after the colon
print(a_dict)
print(a_dict[1])

a_dict = {"name":"MK","Address":"Athens"}
print(a_dict["name"])

print("name" in a_dict)

a_list = [1,2,3]
print(4 in a_list)
print("MK" in a_dict) #Can't find the values, just the keys
print(list(a_dict.keys()))
print(list(a_dict.values()))
print("MK" in list(a_dict.values()))








