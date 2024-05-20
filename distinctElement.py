def d_list(n):                          
    l = []
    for i in n:
        if i not in l:
            l.append(i)
    return l
print(d_list([1,2,2,3,3,34,5,6]))
