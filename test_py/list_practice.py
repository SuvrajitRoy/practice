# thislist = ["apple", "banana", "cherry"]
# print(thislist)

# thislist = ["apple", "banana", "cherry", "apple", "cherry"]
# print(thislist)

# thislist = ["apple", "banana", "cherry"]
# print(len(thislist))      #List Length

# mylist = ["apple", "banana", "cherry"]
# print(type(mylist)) #type

# thislist = list(("apple", "banana", "cherry")) # note the double round-brackets
# print(thislist)       #list() Constructor
# print(thislist[1])    #Access Items
# print(thislist[-1])   #Negative Indexing

# thislist = ["apple", "banana", "cherry"]
# thislist[1] = "blackcurrant"
# print(thislist)

# thislist = ["apple", "banana", "cherry"]
# thislist[1:2] = ["blackcurrant", "watermelon"]    #Range of Indexes   
# print(thislist)

# thislist = ["apple", "banana", "cherry"]
# thislist[1:3] = ["watermelon"]  #Change the second and third value by replacing it with one value:
# print(thislist)

# thislist = ["apple", "banana", "cherry"]
# thislist.insert(2, "watermelon")  #Insert Items
# print(thislist)

thislist = ["apple", "banana", "cherry"]
thislist.append("orange")   #Append Items
print(thislist)

# thislist = ["apple", "banana", "cherry"]
# tropical = ["mango", "pineapple", "papaya"]
# thislist.extend(tropical)     #Extend List
# print(thislist)

# thislist = ["apple", "banana", "cherry", "banana", "kiwi"]
# thislist.pop(1)   #Remove Specified Index
# thislist.pop()
# thislist.clear()  #Clear the List
# del thislist[0]
# del thislist
# thislist.remove("banana")     #Remove Specified Item
# print(thislist)

# thislist = ["apple", "banana", "cherry"]
# for x in thislist:
#   print(x)
  
# for i in range(len(thislist)):    #Loop Through the Index Numbers
#   print(thislist[i])


# i = 0
# while i < len(thislist):      #Using a While Loop
#   print(thislist[i])
#   i = i + 1
  
#   list comprehension 
# fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

# newlist = [x for x in fruits if "a" in x]

# print(newlist)

# newlist = [x for x in range(10)]
# print(newlist)

# thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
# thislist.sort()        # ascending, by default
# print(thislist)

# thislist = [100, 50, 65, 82, 23]
# thislist.sort(reverse = True)  # descending
# print(thislist)

# def myfunc(n):
#   return abs(n - 50)        #Sort the list based on how close the number is to 50

# thislist = [100, 50, 65, 82, 23]
# thislist.sort(key = myfunc)
# print(thislist)

# thislist = ["banana", "Orange", "Kiwi", "cherry"]
# thislist.sort(key = str.lower)
# print(thislist)

# thislist.reverse()
# print(thislist)

# thislist = ["apple", "banana", "cherry"]
# mylist = thislist.copy()      #Copy a List
# print(mylist)

# thislist = ["apple", "banana", "cherry"]
# mylist = thislist[:]      #Use the slice Operator
# print(mylist)

# list1 = ["a", "b", "c"]
# list2 = [1, 2, 3]

# list3 = list1 + list2     #Join Two Lists
# print(list3)

# list1 = ["a", "b" , "c"]
# list2 = [1, 2, 3]

# for x in list2:
#   list1.append(x)

# print(list1)

# list1 = ["a", "b" , "c"]
# list2 = [1, 2, 3]

# list1.extend(list2)
# print(list1)