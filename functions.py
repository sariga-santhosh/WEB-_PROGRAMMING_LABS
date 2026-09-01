def star(n):
    for i in range(1,n+1):
        print("*"*i)
    for i in range(n-1,0,-1):
        print("*"*i)

#star(4)


def character_frequency(string,character):
    frequency = string.count(character)
    return frequency

#print(character_frequency("Sariga","a"))


