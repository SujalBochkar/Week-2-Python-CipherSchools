user_info = {
    'name' : 'Suphal',
    'age' : 24,
    'fav_movies' : ['MH','Got','All of'],
    'fav_tunes': ['sia','one','alone','as was'],
}

more_info = {'name': 'Bochkar','State' : 'Telangana' , 'hobbies' : ['coding','reading','guitar']}

user_info.update(more_info)
user_info.update({})
print(user_info)

