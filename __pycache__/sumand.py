def sumandpair(list):
    size=len(list)
    count=0
    for i in range(0,size):
        for j in range(i+1,size):
            if list[i]==list[j] and (list[i]+list[j])%2==0:
                count+=1
    print("pair is  ", count)
N=5
list=[2,1,3,2,1]
sumandpair(list)

                