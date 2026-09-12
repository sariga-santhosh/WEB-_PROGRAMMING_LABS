a = int(input("Enter 1st number: "))
b = int(input("Enter 2nd number: "))
operator = input("Enter operator (+,-,*,/)")
match operator:
    case "+":
        print(a+b)
    case "-":
        print(a-b)
    case "*":
        print(a*b)
    case "/":
        print(a/b)
    case _:
        print("Invalid Operator")