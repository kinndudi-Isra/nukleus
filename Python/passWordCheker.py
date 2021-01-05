#pass checker
#geting user's informations

password = input(' enter the user\'s password')
userName = input(' what\'s you\'re name')

#hidding user's password
password_length = len(password)
password_hidden = '*' * password_length

print(f'{userName}, your pasword is {password_hidden} ')

