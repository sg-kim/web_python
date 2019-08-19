user_id = input('id? ')
user_pwd = input('password? ')

'''
user_input = input('password? ')
if user_input == '111111':
	print('Welcome')
else:
	print('Wrong password')
'''

'''
if user_id == 'quanto':
	if user_pwd == '111111':
		print('Welcome')
	else:
		print('Who are you?')
else:
	print('Who are you?')
'''

if user_id == 'quanto' and user_pwd == '111111':
	print('Welcome')
elif user_id == 'reizel' and user_pwd == '222222':
	print('Welcome')
else:
	print('Who are you?')

