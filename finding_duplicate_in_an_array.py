
def duplicate(li):
    n =len(li)
    repeat =[]
    for i in range(0,n):
        for j in range(i+1,n):
            if li[i]==li[j] and li[i] not in repeat:
                repeat.append(li[i])
    return repeat



arr =[1,2,3,5,1,2,3]
print(duplicate(arr))