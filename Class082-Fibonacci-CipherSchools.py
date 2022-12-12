def fibonaci(x):
    a = 0
    b = 1
    if x == 1 :
        print(a)
    if x == 2 :
        print(a , b)
    else :
        print(a,b,end=" ")
        for i in range (x-2):
            c = a+b
            a = b
            b = c
            print(b , end = " ")
x = int(input("Write the number you want to print to:"))
fibonaci(x)