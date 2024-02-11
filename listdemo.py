#list are data typle created using []
#items can be duplicated
#list can be converted to tuple using tuple(list1)
#list methods
import random
name=["a","b","c","d","e"]
#name=("a","b","c","d")
total=len(name)
print(total)
# random number generation
number=random.randint(0,total)
print(name[number])
# list methods
# name="Hello"
# print(name[::-1])
users = ['Tom', 'John', 'Sara','kate']

data = ['Tom', 42, True]

# emptylist = []

print("To" in users)

# print(users[0])
# print(users[::-1])
# users.append(data)
# print(users)
print(users.index('Sara'))

# print(users[0:2])
# print(users[1:])
# print(users[-3:-1])

# print(len(data))

# users.append('Elsa')
# print(users)
new_users=['Jason','Mike']
# users.append(new_users)
# print(users)

# users.extend(['Robert', 'Jimmy'])
# print(users)

# # users.extend(data)
# # print(users)
users = ['Tom', 'John', 'Sara','kate']

users.insert(0, 'Bob')
print(users)

# users[2:2] = ['Eddie', 'Alex']
# # print(users)

# users[1:3] = ['Robert', 'JPJ']
# print(users)

print(users.remove('Bob'))
# print(users)

# print(users.pop())
# print(users)

# del users[0]
# print(users)

# # del data
# data.clear()
# print(data)

users[1:2] = ['Tom']
users.sort()
print(users)

# users.sort(key=str.lower)
# print(users)

# nums = [4, 42, 78, 1, 5]
# nums.reverse()
# print(nums)

# # nums.sort(reverse=True)
# # print(nums)

# print(sorted(nums, reverse=True))
# print(nums)

# numscopy = nums.copy()
# mynums = list(nums)
# mycopy = nums[:]

# print(numscopy)
# print(mynums)
# mycopy.sort()
# print(mycopy)
# print(nums)

# print(type(nums))

# mylist = list([1, "Neil", True])
# print(mylist)
 