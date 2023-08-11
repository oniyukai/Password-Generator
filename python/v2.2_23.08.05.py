import random

print('----\nPassword Generator\nVersion 2.2_23.08.05\nhttps://github.com/oniyukai/Password-Generator\n----\n')
askings = ('Whether to include 0-9? [Y/N] ', 'Whether to include a-z? [Y/N] ', 'Whether to include A-Z? [Y/N] ', 'Whether to include !@#$%^&* ? [Y/N] ')
include = ('0123456789', 'abcdefghijklmnopqrstuvwxyz', 'ABCDEFGHIJKLMNOPQRSTUVWXYZ', '!@#$%^&*')

while True:
    characters = ''
    length = input('\nInput the length of password: ')
    sets = input('Input several sets of generated passwords: ')
    for i in range(4):
        answer = input(askings[i])
        characters += include[i] if answer=='Y' or answer=='y' else ''
    answer = input('Whether to input additions? [Y/N] ')
    characters += input('Input additions: ') if answer=='Y' or answer=='y' else ''
    print('\nGenerated password:')
    for i in range(int(sets)):
        print(''.join(random.choices(characters, k=int(length))))
