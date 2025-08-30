# def my_function():
#   print("Hello from a function")

# my_function()

# def my_function(fname):     #Arguments
#   print(fname + " Refsnes")

# my_function("Emil")
# my_function("Tobias")
# my_function("Linus")


# def my_function(fname, lname):      #Number of Arguments
#   print(fname + " " + lname)

# my_function("Emil", "Refsnes")

# def my_function(*kids):     #Arbitrary Arguments, *args
#   print("The youngest child is " + kids[2])

# my_function("Emil", "Tobias", "Linus")

# def my_function(child3, child2, child1):
#   print("The youngest child is " + child3)

# my_function(child1 = "Emil", child2 = "Tobias", child3 = "Linus")       #Keyword Arguments

# def my_function(**kid):     #Arbitrary Keyword Arguments, **kwargs
#   print("His last name is " + kid["lname"])
# my_function(fname = "Tobias", lname = "Refsnes")

# def my_function(country = "Norway"):        #Default Parameter Value
#   print("I am from " + country)
# my_function("Sweden")
# my_function("India")
# my_function()
# my_function("Brazil")

# def my_function(food):
#   for x in food:        #Passing a List as an Argument
#     print(x)
# fruits = ["apple", "banana", "cherry"]
# my_function(fruits)

def my_function(x):
  return 5 * x      #Return Values
print(my_function(3))
print(my_function(5))
print(my_function(9))


def tri_recursion(k):       #Recursion
  if(k > 0):
    result = k + tri_recursion(k - 1)
    print(result)
  else:
    result = 0
  return result

print("Recursion Example Results:")
tri_recursion(6)