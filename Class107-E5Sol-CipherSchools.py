def common(a,b):
    com=[]
    for i in a:
        for j in b:
            if i==j : com+=[i]
    return com

input1=[1,2,3,4]
input2=[1,2,5,4]

print(common(input1,input2))

