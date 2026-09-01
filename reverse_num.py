num = int(input("Enter a number:"))

rev_number = 0

while num != 0:
    reminder = num % 10
    num = num // 10
    rev_number = rev_number * 10 + reminder

print(rev_number)