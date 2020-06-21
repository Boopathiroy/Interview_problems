
#TO check a number prime or not

def prime(num):
    flag =0
    for i in range(2,(num//2)+1):
        if num%i == 0:
            flag =1
            return False
    if flag ==0:
        return True

number = 4
print(prime(number))