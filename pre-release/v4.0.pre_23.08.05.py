import random

print('----\nPassword Generator\nVersion 4.0.pre_23.08.05\nhttps://github.com/oniyukai/Password-Generator\n----')
askings = ('Whether to include 0-9? [Y/N] ', 'Whether to include a-z? [Y/N] ', 'Whether to include A-Z? [Y/N] ', 'Whether to include !@#$%^&* ? [Y/N] ')
include = ('0123456789', 'abcdefghijklmnopqrstuvwxyz', 'ABCDEFGHIJKLMNOPQRSTUVWXYZ', '!@#$%^&*')
max_section = 4

while True:
    sets = ['' for i in range(int(input('\n\nInput several sets of generated passwords: ')))]
    sections = input(f'Input the several sections of the password (Up to {int(max_section)} sections): ')
    while True:
        if int(sections) > max_section or int(sections) < 1:
            sections = input('Error, please input another response again: ')
        else:
            break
    for i in range(int(sections)):
        print('\nSetting the ' + str(i+1) + '/' + sections + ' section:')
        length = input('Input the length of this section: ')
        characters = ''
        for j in range(4):
            answer = input(askings[j])
            characters += include[j] if answer=='Y' or answer=='y' else ''
        answer = input('Whether to input additions? [Y/N] ')
        characters += input('Input additions: ') if answer=='Y' or answer=='y' else ''
        for j in range(int(len(sets))):
            sets[j] += ''.join(random.choices(characters, k = int(length)))
    print('\nGenerated password:')
    for i in range(int(len(sets))):
        print(sets[i])