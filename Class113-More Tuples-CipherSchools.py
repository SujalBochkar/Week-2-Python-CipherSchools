# looping in tuples
# tuple with one element
# tuple without parenthesis
# tuple unpacking
# list inside tuple
# some functions that you can use with tuples
mixed =(1,2,8,6.5,4.0)

#~ for loop and tuple
# for i in mixed:
#     print(i)
# NOTE - You can use while loop too
 
 
   
#~ tuple with one element
# nums =(1)                  #! not a tuple
# print(type(nums))
# nums =(1,)                 #! it's a tuple
# print(type(nums))

# words = ('wordl')          #! not a tuple 
# print(type(words))         #! add Comma(,) to tuple
# words = ('wordl',)         #! it's a tuple
# print(type(words))

#~ tuple without parenthesis
# guitars = 'Iyamaha', 'baton',' rouge','taylor'
# print(type(guitars))

#~ Tuple Unpacking
# names=('Maneli Jamal', 'Eddie','Andrew Foy')
# namel, name2, name3=names
# print(namel)
# print(name2)
# print(name3)


#~ list inside tuples Are Editable
fav=('southern','magnolia',['Tokyo','landscape'])
fav[2].pop()
fav[2].append("Hii")
print(fav)



print(min(mixed))
print(max(mixed))
print(sum(mixed))









