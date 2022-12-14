
#! Zero Division error

#~ Try And Except

def div(a,b):
    try:
        print( a/b)
    except ZeroDivisionError  as aware:
        # print( "Cannot Divied With zero You hero)"
        print( aware)
    except TypeError:
        print("Hiii")
    except :
        print("You made error man")

# a=int(input())
# b=int(input())
div(10,0)
div(10,'2')

