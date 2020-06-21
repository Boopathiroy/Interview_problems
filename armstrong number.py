
#To find the armstrong number
# 153 = 1**3 + 5**3 + 3**3

def armstrong(num):
    temp = num
    sum =0
    while num>0:
        rem = num%10
        sum += rem**3
        num = num//10
    return sum == temp


nmber = 153
print(armstrong(nmber))