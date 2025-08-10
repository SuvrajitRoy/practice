# f = open("demofile.txt", "r")
# print(f.read())


# f = open("D:\\My zone\welcome.txt", "r")

# print(f.read())

# with open("demofile.txt") as f:
#   print(f.readline())
#   f.close()
  
# f = open("demofile.txt", "r")
# print(f.readline())

with open("demofile.txt", "a") as f:
  f.write("Now the file has more content!")

#open and read the file after the appending:
with open("demofile.txt") as f:
  print(f.read())