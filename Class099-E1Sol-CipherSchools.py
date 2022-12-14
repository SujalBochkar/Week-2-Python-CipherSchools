def sq_lis(num):
    sq_num=[]
    for i in num:
        sq_num += [i**2]
    return sq_num

num=list(range(1,11))
print(sq_lis(num))

