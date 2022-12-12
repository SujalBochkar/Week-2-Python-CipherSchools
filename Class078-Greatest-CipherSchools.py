def lowest(a,b,c):
    if a < b and a < c:
        return a
    if b<a and b<c :
        return b
    else :
        return c
print(lowest(10,89,54))