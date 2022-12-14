def list_count(a):
    z=0
    for i in a:
        if type(i) == list : z+=1
    return z

a=[1,2,3,4,[1,3,4,6],3,5,["as","asdf","sd","we","tt"],"as"]
print(list_count(a))
