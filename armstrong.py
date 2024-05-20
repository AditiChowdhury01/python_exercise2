n = int(input("enter number:"))
sum =0
temp = n
while(temp>0):
    rem  = temp%10
    temp = temp//10
    sum = sum + (rem**3)
if (n==sum):
    print("armstrong number")
else:
    print("not an armstrong number")