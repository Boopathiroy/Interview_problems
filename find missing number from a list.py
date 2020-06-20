
li =[1,2,3,4,6,7,8,9,10]

n = len(li)
total = (n+1)*(n+2)//2
sum_of_li = sum(li)
missing_number = total-sum_of_li

print(missing_number)
