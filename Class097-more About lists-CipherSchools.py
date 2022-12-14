# Generate lists with range functions
# more about pop
# index method
# pass list to a function

# num=list(range(1,11))
num=[1,2,3,4,5,6,7,8,9,10,1]
# print(num)

# print(num.pop())        #! uses to print popped item
# popped_item=num.pop()
# print(popped_item)
# print(num)


#^ To find particular item index
#~ index Syntax   .index({to find},{start},{stop})

print(num.index(1,3,14))         

def negtive(l):
    neg=[]
    for i in l:
        # neg.append(-i)
        neg+=[-i]
    return neg

print(negtive(num))


