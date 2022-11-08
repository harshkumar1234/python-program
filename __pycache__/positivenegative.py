# find number of pair positive and negative in the list 
# list=[2,-2,1,4,-2]
# out= 
# y  positive pair nomber is= 6
# x  positive pair nomber is= 9

def posneg(arr):
    res=1
    x=0
    y=0
    for i in range(1,len(arr)+1):
        for j in range(i,len(arr)):
            arr[i]=i*arr[j]
            if arr[i]<0:
                x+=1
            if arr[i]>0:
                y+=1
            print(arr[i])
    # return x,y 
    print("x negpair is ", x)
    print("y pospair is ", y)


list=[2,-2,1,4,-2]
print(posneg(list))