# #n Python, closure is created by nesting a function inside another encapsulating function and then returning the inner function.

# def add_ten():
#     ten = 10
#     def add(num):
#         print(num)
#         return num + ten
      
#     return add

# closure_result = add_ten()
# print(closure_result(5))

# #example2

def power_of(n):
    def exponent(x):
        return x ** n
    return exponent

# Create closures for squaring and cubing
square_closure = power_of(2)
cube_closure = power_of(3)

print(square_closure(4))  # Output: 16
print(cube_closure(3))    # Output: 27
#example3

# def hello():
#     print("hello",end=" ")
#     def name(name):
#         print(name)
#     return name
# closure_name=hello()  
# closure_name("nisha")

# def fname(fname):
#     def lname(lname):
#         print(f"{fname}{lname}")
#     return lname

# name=fname("john")
# name("Joes")