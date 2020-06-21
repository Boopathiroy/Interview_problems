
#TO find the prime numbrs in an interval

def prime_number(f,l):

    while f<l:
        flag =0
        for i in range(2,(f//2)+1):
            if(f%i)==0:
                flag =1
                break
        if(flag==0):
             print(f,end=' ')
        f+=1

inital = 1
last = 20
prime_number(inital,last)
