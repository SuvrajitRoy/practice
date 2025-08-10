# thistuple = ("apple", "banana", "cherry")
# print(thistuple)

# thistuple = ("apple", "banana", "cherry")
# print(len(thistuple))   #Tuple Length

# thistuple = ("apple",)
# print(type(thistuple))

# #NOT a tuple
# thistuple = ("apple")
# print(type(thistuple))

# thistuple = ("apple", "banana", "cherry")
# print(thistuple[1])     #Access Tuple Items

# thistuple = ("apple", "banana", "cherry")
# print(thistuple[-1])        #Negative Indexing

# thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
# print(thistuple[2:5])       #Range of Indexes
# print(thistuple[:4])
# print(thistuple[-4:-1])     #Range of Negative Indexes

# thistuple = ("apple", "banana", "cherry")
# if "apple" in thistuple:        #Check if Item Exists
#   print("Yes, 'apple' is in the fruits tuple")

# x = ("apple", "banana", "cherry")
# y = list(x)
# y[1] = "kiwi"       #Change Tuple Values
# x = tuple(y)
# print(x)


# thistuple = ("apple", "banana", "cherry")
# y = list(thistuple)
# y.append("orange")      #Add Items
# thistuple = tuple(y)
# print(thistuple)

# thistuple = ("apple", "banana", "cherry")
# y = list(thistuple)
# y.remove("apple")       #Remove Items
# thistuple = tuple(y)
# print(thistuple)

# fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")
# (green, yellow, *red) = fruits      #Using Asterisk*
# print(green)
# print(yellow)
# print(red)

# thistuple = ("apple", "banana", "cherry")
# for x in thistuple:     #Loop Through a Tuple
#   print(x)

# thistuple = ("apple", "banana", "cherry")
# for i in range(len(thistuple)):     #Loop Through the Index Numbers
#   print(thistuple[i])

# thistuple = ("apple", "banana", "cherry")
# i = 0
# while i < len(thistuple):       #Using a While Loop
#   print(thistuple[i])
#   i = i + 1

# tuple1 = ("a", "b" , "c")
# tuple2 = (1, 2, 3)
# tuple3 = tuple1 + tuple2        #Join Two Tuples
# print(tuple3)  

fruits = ("apple", "banana", "cherry")
mytuple = fruits * 2        #Multiply Tuples

print(mytuple)