# write in file using with() function
with open("sample.txt", "w") as file:
    file.write("Hi! I am Penguin and I am 1 year old.")
file.close()


# split() function
with open("sample.txt", "r") as file:
   data = file.readlines()
   print("Words in this file are.... ")
   for line in data:
       words = line.split()
       print (words)

file.close()
