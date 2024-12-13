import random

print('----\nPassword Generator\nVersion 4.0.pre_23.08.02\nhttps://github.com/oniyukai/Password-Generator\n----')
askings = ['Whether to add 0-9? [Y/N] ', 'Whether to add a-z? [Y/N] ', 'Whether to add A-Z? [Y/N] ', 'Whether to add \'!@#$\%^&*\' ? [Y/N] ']
character = ['0123456789', 'abcdefghijklmnopqrstuvwxyz', 'ABCDEFGHIJKLMNOPQRSTUVWXYZ', '!@#$%^&*']
max_section = 4

while True:
    password = []
    section = input(f'\n\nEnter the several sections of the password(Up to {int(max_section)} sections): ')
    while True:
        if int(section) > 0 and int(section) < max_section+1:
            break
        else:
            section = input('Error, please enter another response again: ')
    sets = input('Enter several sets of generated passwords: ')
    for i in range(int(sets)):
        password.append('')
    for i in range(int(section)):
        print('\nSetting the ' + str(i+1) + '/' + section + ' section:')
        data = ''
        long = input('Enter the length of this section: ')
        for j in range(4):
            answer = input(askings[j])
            if answer == 'Y' or answer == 'y':
                data += character[j]
        answer = input('Whether to enter characters outside? [Y/N] ')
        if answer == 'Y' or answer == 'y':
            answer = input('Enter the outer characters: ')
            data += answer
        for j in range(int(sets)):
            password[j] += ''.join(random.choices(data, k = int(long)))
    print('\nGenerated password:')
    for i in range(int(sets)):
        print(password[i])