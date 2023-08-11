import random

print('----\nPassword Generator\nVersion 4.0_23.08.05\nhttps://github.com/oniyukai/Password-Generator\n----')
askings = ('Whether to include 0-9? [Y/N] ', 'Whether to include a-z? [Y/N] ', 'Whether to include A-Z? [Y/N] ', 'Whether to include !@#$%^&* ? [Y/N] ')
include = ('0123456789', 'abcdefghijklmnopqrstuvwxyz', 'ABCDEFGHIJKLMNOPQRSTUVWXYZ', '!@#$%^&*')
max_section = 4

while True:
    sets = input('\n\nInput several sets of generated passwords: ')
    sections = input(f'Input the several sections of the password (Up to {int(max_section)} sections): ')
    while True:
        if int(sections) > max_section or int(sections) < 1:
            sections = input('Error, please input another response again: ')
        else:
            break
    sections = ['' for i in range(int(sections))]
    sections_length = []
    for i in range(len(sections)):
        print('\nSetting the ' + str(i+1) + '/' + str(len(sections)) + ' section:')
        sections_length.append(input('Input the length of this section: '))
        for j in range(4):
            answer = input(askings[j])
            sections[i] += include[j] if answer=='Y' or answer=='y' else ''
        answer = input('Whether to input additions? [Y/N] ')
        sections[i] += input('Input additions: ') if answer=='Y' or answer=='y' else ''
    print('\nGenerated password:')
    for i in range(int(sets)):
        for j in range(len(sections)):
            print(''.join(random.choices(sections[j], k=int(sections_length[j]))), end='')
        print()
