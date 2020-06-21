
#Factorial of a number

def fact(num):
    total=1
    while num>0:
        total *=num
        num= num-1
    return total

number = 3
print(fact(number))