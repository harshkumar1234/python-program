from itertools import count


def countsub(num):
    set1=set(num)
    for i in range(len(num)):
        for j in range(i+1,len(num)+1):
            set1.add(num[i:j])
    size=len(set1)
    list1=list(set1)
    res=0
    for i in range(len(list1)):
        res +=list1[i].count('1')
    return res 
num="0100"
print(countsub(num))