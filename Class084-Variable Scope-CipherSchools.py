x=5      #! Global Variable
def func():
    global x    #! To use as global variable
    x=7         #! Local Variable
    return x

print(x)        #! func() is not yet called do x=5
print(func())   #! it is called and x=7
print(x)        #! x=7