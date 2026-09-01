string = input("Input your fullname:")
print(string.upper()) 
print(string.lower())
print(string.title())
print(string.title().replace(" ",""))

#d = input("Input ur course:")
#  sariga santhoshb print(string +" " + d)
print(len(string))
print(string[3])
print(string[0:4])
list_of_names = string.split(" ")
first_name = str(list_of_names[0])
last_name = str(list_of_names[1])
print(first_name)
print(last_name)
print(string.replace("a","f"))
print(string.replace(" ","*"))
print(string.strip())
odd_str = []
for i in range(len(string)):
    if i % 2 != 0:
        odd_str.append(string[i])
print("".join(odd_str))
print(string.count("a"))
print(string.find("o"))

    
