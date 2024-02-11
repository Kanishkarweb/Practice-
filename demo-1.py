a = 5
if a > 0:
    print('A is a positive number')
    
# syntax
# if condition:
#     this part of code runs for truthy conditions
# else:
#      this part of code runs for false conditions

a = "3"
if int(a) < 0:
    print('A is a negative number')

else:
    print('A is a positive number')
    
#multiple condition elif

# syntax
# if condition:
#     code
# elif condition:
#     code
# else:
#     code


a = 0
if a > 0:
    print('A is a positive number')
elif a < 0:
    print('A is a negative number')
else:
    print('A is zero')

#short hand  
# syntax
# code if condition else code    

a = 3
print('A is positive') if a > 0 else print('A is negative') # first condition met, 'A is positive' will be printed

#nested ifs

# syntax
# if condition:
#     code
#     if condition:
#     code
    
a = 5
if a > 0:
    if a % 2 == 0:
        print('A is a positive and even integer')
    else:
        print('A is a positive number')
elif a == 0:
    print('A is zero')
else:
    print('A is a negative number')
    
#logical operators and-both conndition true,or any one true,not opposit

a = 5
if a > 0 and a % 2 == 0:
    print('A is an even and positive integer')
elif a > 0 or a % 2 !=  0:
     print('A is a positive integer')
elif a == 0:
    print('A is zero')
else:
    print('A is negative')
    
    
# user = 'James'
# access_level = 3
# if user == 'admin' or access_level >= 4:
#         print('Access granted!')
# else:
#     print('Access denied!')