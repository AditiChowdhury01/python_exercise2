def case(str):                     
    x = 0
    count = 0
    for i in str:
       if i.isupper() :
        count = count+1
       elif i.islower():
        x = x+1
       else:
         pass
    print("no. of upper case letters are",count)
    print("no. of lower case letters are",x)
case("A quick Brown Fox")