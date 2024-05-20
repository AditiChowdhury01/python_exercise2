def perfect(n):                      
    sum =0
    for i in range(1,n):
        if n%i==0:
            sum = sum+i
    if(sum==n):
       print("perfect!!!")  
perfect(6)