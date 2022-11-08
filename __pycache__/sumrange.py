# t=1
# q=2
# r=3
# l=1
# list1=[6,7]
# list2=[9,9]
# out= 1 and 0

def sumrange1(t,q,l,r,list1,list2):
    list=r-l+1
    # print(list)
    res=0
    for n in range(1,list+1):
        res+=n
    # print(res)
    if res in list1:
        print(1)
    else:
        print(0)
    if res in list2:
        print(1)
    else:
        print(0)
if __name__ == '__main__':
    
    t=1
    q=2
    r=3
    l=1
    list1=[6,7]
    list2=[9,9]
    sumrange1(t,q,l,r,list1,list2)