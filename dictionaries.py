a_dict = {"k1":5,"k2":7,1:"hello"} #Curly braces are used for dictionaries and sets #key is in quotes and value is after the colon
print(a_dict)
print(a_dict[1])

a_dict = {"name":"MK","Address":"Athens"}
#a_dict.update({"Phone":"704-929-4843"}) #adds more keys or dictionaries
#or
a_dict["Phone"] = "704-929-4843"
print(a_dict)
print("Ok")
print(a_dict["name"])
print("Ok1")
print(list(a_dict.items())[2])
print("Ok2")
print(list(a_dict.keys()))
print("ok3")

a_dict = {}
a_dict["key1"] = {}
a_dict["key2"] = {}

a_dict["key1"]["values"] = []
a_dict["key1"]["single_value"] = 3

a_dict["key1"]["values"].append(4)
print(a_dict)


print("name" in a_dict)

a_list = [1,2,3]
print("ok123")
print(4 in a_list)
print("MK" in a_dict) #Can't find the values, just the keys
print(list(a_dict.keys()))
print(list(a_dict.values()))
print("MK" in list(a_dict.values()))








