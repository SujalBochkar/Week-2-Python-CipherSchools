
# def reverse(l):
#     l.reverse()
#     return l

# def reverse(l):
#     return l[::-1]

def reverse(li):
    z=[]
    for i in range(len(li)):
        z+=[li.pop()]    
    return z


num=list(range(1,11))
print(reverse(num))

