# program without recursion

# def find_sum(n):
#     sum=0
#     for a in range(1,n+1):
#         sum+=a
    
#     return sum

# if __name__=='__main__':
#     print(find_sum(5))
# output=15

#program with recursion

# def find_sum(n):
#     if n==1:
#         return 1
#     return n+ find_sum(n-1)

# if __name__=='__main__':
#     print(find_sum(5))
#     #output=15

#      fibonnassi series
# def fib(n):
#     if n==1 or n==0:
#         return n
#     return fib(n-1) + fib(n-2)

# if __name__=='__main__':
#     print(fib(6))
