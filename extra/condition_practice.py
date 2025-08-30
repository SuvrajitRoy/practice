# a = 33
# b = 200
# if b > a:       #If ... Else
#   print("b is greater than a")

# a = 33
# b = 33
# if b > a:
#   print("b is greater than a")
# elif a == b:        #Elif
#   print("a and b are equal")
# else:
#   print("a is greater than b")

# a = 2
# b = 330
# print("A") if a > b else print("=") if a == b else print("B")     #Short Hand If ... Else

# a = 200
# b = 33
# c = 500
# if a > b and c > a:
#   print("Both conditions are True")

# elif a > b or a > c:
#   print("At least one of the conditions is True")

# elif not a > b:
#   print("a is NOT greater than b")

# a = 33
# b = 200
# if b > a:
#   pass
# # having an empty if statement like this, would raise an error without the pass statement

# day = 4
# match day:      #Match Statement
#   case 1:
#     print("Monday")
#   case 2:
#     print("Tuesday")
#   case 3:
#     print("Wednesday")
#   case 4:
#     print("Thursday")
#   case 5:
#     print("Friday")
#   case 6:
#     print("Saturday")
#   case 7:
#     print("Sunday")

# day = 4
# match day:
#   case 6:
#     print("Today is Saturday")
#   case 7:
#     print("Today is Sunday")
#   case _:       #Default Value
#     print("Looking forward to the Weekend")

# day = 4
# match day:
#   case 1 | 2 | 3 | 4 | 5:       #Combine Values
#     print("Today is a weekday")
#   case 6 | 7:
#     print("I love weekends!")

# month = 5
# day = 4
# match day:
#   case 1 | 2 | 3 | 4 | 5 if month == 4:     #If Statements as Guards
#     print("A weekday in April")
#   case 1 | 2 | 3 | 4 | 5 if month == 5:
#     print("A weekday in May")
#   case _:
#     print("No match")

# i = 1
# while i < 6:        #While Loop
#   print(i)
#   i += 1

# i = 1
# while i < 6:
#   print(i)
#   if i == 3:
#     break       #break Statement
#   i += 1

# i = 0
# while i < 6:
#   i += 1
#   if i == 3:
#     continue        #Continue Statement
#   print(i)

# fruits = ["apple", "banana", "cherry"]
# for x in fruits:        #For Loops
#   print(x)

# fruits = ["apple", "banana", "cherry"]
# for x in fruits:
#   print(x)
#   if x == "banana":
#     break
  
# fruits = ["apple", "banana", "cherry"]
# for x in fruits:
#   if x == "banana":
#     continue
#   print(x)

# for x in range(6):
#   print(x)

# for x in range(2, 6):
#   print(x)

# for x in range(2, 30, 3):
#   print(x)

# for x in range(6):
#   print(x)
# else:
#   print("Finally finished!")

adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]
for x in adj:
  for y in fruits:      #Nested Loops
    print(x, y)