
#~ From Keys  (to have values of keys)

# a=dict.fromkeys(['name','age','height'],'unknown')
# print(a)
# b=dict.fromkeys("abc",'unknown')
# print(b)
# c=dict.fromkeys(range(1,11),'unknown')
# print(c)
# d=dict.fromkeys(['name','age'],['unknown','unknown'])
# print(d)

#~ Get Method
d={'name':'unkssnown','age':'unknown'}

# print(d['name'])
# print(d.get('name'))
# print(d.get('names'))
# if d.get('name'):
#     print("Present")
# else:
#     print("Not Present")

#~ Clear Dict
# d.clear()
# print(d)

#! "=" is same as d and d1
d1=d.copy()
d2=d
# d.popitem()
# print(d)
# print(d1)
# print(d2)

print(d1 is d)
print(d2 is d)
print(d1 == d)
print(d2 == d)



