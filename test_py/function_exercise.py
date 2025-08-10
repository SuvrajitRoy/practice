# def my_function():
#   print("Hello from a function")

# my_function()        #Calling a Function

# def my_function(fname):   #Parameters
#   print(fname + " Refsnes") #Arguments

# my_function("Emil")
# my_function("Tobias")
# my_function("Linus")

# def my_function(fname, lname):
#   print(fname + " " + lname)

# my_function("Emil", "Refsnes")

# def my_function(*kids):    #Arbitrary Arguments, *args
#   print("The youngest child is " + kids[2])

# my_function("Emil", "Tobias", "Linus")

# def my_function(child3, child2, child1):  #Keyword Arguments
#   print("The youngest child is " + child3)

# my_function(child1 = "Emil", child2 = "Tobias", child3 = "Linus")

# def my_function(food):
#   for x in food:
#     print(x)

# fruits = ["apple", "banana", "cherry"]      #Passing a List as an Argument

# my_function(fruits)

# def my_function(x):   #Return Values
#   return 5 * x

# print(my_function(3))
# print(my_function(5))

# def tri_recursion(k):    #Recursion Example
#   if(k > 0):
#     result = k + tri_recursion(k - 1)
#     print(result)
#   else:
#     result = 0
#   return result

# print("Recursion Example Results:")
# tri_recursion(6)

# x = lambda a, b : a * b     #Lambda function
# print(x(5, 6))

def myfunc(n):
  return lambda a : a * n

mydoubler = myfunc(2)

print(mydoubler(11))