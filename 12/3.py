print('Изменение списка')
users = ['Admin', 'Guest', 'User', 'Bot']
users[2] = 'Moderator'
users[3] = 'SuperAdmin'
users.append('Newbie')
print(*users, sep = ', ')
