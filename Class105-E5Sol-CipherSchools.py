def even_odd(a):
    odd=[]
    even=[]
    for i in a:
        if int(i)%2 == 0:  even+=[i]
        else: odd+=[i]
    
    # return [odd] + [even]
    return [odd,even]

put=list(range(1,8))
print(even_odd(put))
