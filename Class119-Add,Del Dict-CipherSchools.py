user_info = {
    'name' : 'Suphal',
    'age' : 24,
    'fav_movies' : ['MH','Got','Squid','ST','All of'],
    'fav_tunes': ['sia','one','unstop','safari','faded','alone','as it was'],
}

#~ Add Data
# user_info['fav_songs'] = ['songs1','songs2']
# print(user_info)


#~ Pop method 
popped=user_info.pop('age')
print(f'popped is {popped}')
print(type(popped))
print(user_info)

#~ Pop item method 
popped_item = user_info.popitem()
print(popped_item)
print(type(popped_item))
print(user_info)
