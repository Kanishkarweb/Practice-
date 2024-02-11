letter = 'P'                # A string could be a single character or a bunch of texts
print(letter)               # P
print(len(letter))          # 1
greeting = 'Hello, World!'  # String could be made using a single or double quote,"Hello, World!"
print(greeting)             # Hello, World!
print(len(greeting))        # 13

multiline_string = '''I am a teacher and enjoy teaching.
I didn't find anything as rewarding as empowering people.
That is why I created 30 days of python.'''
print(multiline_string)

first_name = 'John'
last_name = 'Josh'
space = ' '
full_name = first_name  +  space + last_name
print(full_name) 
# Checking the length of a string using len() built-in function
print(len(first_name))  
print(len(last_name))   
print(len(first_name) > len(last_name)) # True or False
print(len(full_name)) 

# Strings Formatting
first_name = 'John'
last_name = 'Jpsh'
language = 'Python'
formated_string = 'I am %s %s. I teach %s' %(first_name, last_name, language)
print(formated_string)

# Strings  and numbers
radius = 10
pi = 3.14
area = pi * radius ** 2
formated_string = 'The area of circle with a radius %d is %.2f.' %(radius, area) # 2 refers the 2 significant digits after the point

python_libraries = ['Django', 'Flask', 'NumPy', 'Matplotlib','Pandas']
formated_string = 'The following are python libraries:%s' % (python_libraries)
print(formated_string) 

#string format using format
a = 4
b = 3

print('{} + {} = {}'.format(a, b, a + b))#4 + 3 = 7
print('{} - {} = {}'.format(a, b, a - b))# 4 - 3 = 1

#f-strings

a = 4
b = 3
print(f'{a} + {b} = {a +b}')#4 + 3 = 7
print(f'{a} - {b} = {a - b}')# 4 - 3 = 1

#slicing
language = 'Python'
first_three = language[0:3] # starts at zero index and up to 3 but not include 3
print(first_three) #Pyt
last_three = language[3:6]
print(last_three) # hon
# Another way
last_three = language[-3:]
print(last_three)   # hon
last_three = language[3:]
print(last_three)   # hon

#reverse string
greeting = 'Hello, World!'
print(greeting[::-1]) # !dlroW ,olleH

#string methods
#capitalize
challenge = 'thirty days of python'
print(challenge.capitalize()) # 'Thirty days of python'

#count
challenge = 'thirty days of python'
print(challenge.count('y')) # 3

#endswith
challenge = 'thirty days of python'
print(challenge.endswith('on'))   # True

#strip(): Removes all given characters starting from the beginning and end of the string
challenge = 'thirty days of pythoonnn'
print(challenge.strip('noth')) # 'irty days of py'

#split(): Splits the string, using given string or space as a separator
challenge = 'thirty days of python'
print(challenge.split()) # ['thirty', 'days', 'of', 'python']
