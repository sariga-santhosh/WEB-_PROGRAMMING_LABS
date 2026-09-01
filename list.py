list_input = list(input("Enter a list: "))
print(list_input)

print(sorted(list_input))
print(" ".join(sorted(list_input)))

print(list(reversed(list_input)))

list_input.append(6)
print(list_input)
print(list_input.pop())
print(list_input)

list_input.remove(list_input[0])
print(list_input)

print(len(list_input))

list_input.clear()
print(list_input)

number = 6587457347
print(list(str((number))))

num_to_binary = 10
binary_num = []
quotient = num_to_binary
while quotient != 1:
    quotient = num_to_binary // 2
    binary_num.append(num_to_binary % 2)
    num_to_binary = quotient
binary_num.append(1)
print(binary_num[::-1])

list_of_numbers = [4,5,6,7,9,10]
squared = [i * i for i in list_of_numbers]
print(list_of_numbers)
print(squared)

copied_list = list_of_numbers.copy()
print(copied_list)

number_to_insert = 5
position = 4
list_of_numbers.insert(position,number_to_insert)
print(list_of_numbers)