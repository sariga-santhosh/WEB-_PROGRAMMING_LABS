a = int(input("Enter 1st number :"))
b = int(input("Enter 2nd number :"))
c = int(input("Enter 3rd number :"))
largest = a
if b > largest:
  largest = b
if c > largest:
  largest = c
print(largest)