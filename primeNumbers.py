n = int(input("enter number: "))              
if n>1:
    for i in range(2,n):
        if n%i==0:
            print("not prime number")
            break
    else:
        print("prime number")

#else:
    #print("not prime")