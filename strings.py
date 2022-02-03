
from re import A


a_string = "a double quoted string can contain ''"
another_string = 'a single quoted string can contain ""'
an_escaped_string = "a double quoted string can contain \"\", but \\ must be escaped"
print(a_string);print(another_string);print(an_escaped_string)
a_triple_quoted_string = '''something
something else that can extend to multiple lines
something else
else'''
print(a_triple_quoted_string)

'''
A triple 
quoted string 
is also like
 writing a multi-line 
 comment
'''

a_formatted_string = f"a normal formatted string can contain variables like {a_string}"
print(a_formatted_string)

a_long_number = 22/7
print(a_long_number)

print(f'{a_long_number:.2f}')

print(f'{a_long_number:.200f}')

a_string = "abc"
b_string = "b"
ab_string = f"{a_string}{b_string}"
print(ab_string)

a_raw_string = r"a raw string can contain \\ characters"
print(a_raw_string)
not_a_raw_string = "a raw string can contain \\ characters"
print(not_a_raw_string)
a_raw_formatted_string = rf"a raw formatted string can still contain other things {a_string}"
print(a_raw_formatted_string)

a_concatenation = "The approcimation of pi is: " + str(a_long_number)
print(a_concatenation)
b_concatenation = f"The approcimation of pi is: + a_long_number"

a_capitalized_string = 'ABC'
a_lowercase_string = a_capitalized_string.lower()
print(a_lowercase_string)

a_string_with_padding = "   3   4   \n" 
print(a_string_with_padding)
print(a_string_with_padding.strip())    #Gets rid of white space in the beginning and end

a_string_as_a_list = list(a_string)
print(a_string_as_a_list)
a_list_as_a_string = "".join(a_string_as_a_list)
print(a_list_as_a_string)
a_string = "hello world"
a_substring = a_string[::-1] #Reverses the string
print(a_substring)
b_substring = a_string[:3]
print(b_substring)
print(len(b_substring))

for i in range(0,len(b_substring)):
    print(b_substring[i])

for c in b_substring:
    print(c)

while True:
    correct_number = 7
    user_input = int(input("Guess a number: "))
    correct = user_input == correct_number
    #print(user_input == correct_number)
    print(correct)
    if correct:
        break
print("great!!!!")

correct_number = 7

while not correct:
    user_input = int(input("Guess a number: "))
    correct = user_input == correct_number
    #print(user_input == correct_number)
    print(correct)
    
print("great!!!!")

