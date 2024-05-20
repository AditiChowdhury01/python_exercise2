
def str_reverse(str1):                       
    rstr = ' '
    index = len(str1)
    while index>0:
        #print(index-1)
        #print(len(str1))
        rstr =rstr + str1[index-1]
        index = index-1
    return rstr
print(str_reverse('1234abcd'))