# Tuples
#Tuples are immutable
#tuples can be duplicated
x=10
print(type(x))
tup1=(1,2,3,4)
mytuple = ('Tom', 42, True)
# print()
#[]->list
anothertuple = (1, 4, 2, 8, 2, 2)
print(len(mytuple))
# mytuple.insert(0,"wdwdwd")
# print(mytuple)

# print(mytuple)
print(type(mytuple))
# print(type(anothertuple))

newlist = list(mytuple)#type conversion

newlist.append('Neil')
print(newlist)
newtuple = tuple(newlist)
# print(newtuple)

(one, *two, hey) = anothertuple
print(one)
print(two)
print(hey)
print(anothertuple)


print(anothertuple.count(2))
# del anothertuple
# print(anothertuple)