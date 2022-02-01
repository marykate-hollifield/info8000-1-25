#print("hello world")
#print("Loading the file")
f = open("test.txt",encoding='utf-8')
lines = f.readlines()
print(lines)
lines = [x.strip() for x in lines]
print(lines)

the_sum = 0

for line in lines:
    print(line)

for line in lines:
    the_sum = the_sum + int(line)
    print(the_sum)

print(sum([int(x) for x in lines]))
print("The sum is",the_sum)
print("The sum is also",sum([int(x) for x in lines]))
print(f"The sum is again {the_sum}")

