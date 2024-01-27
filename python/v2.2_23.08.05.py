import random

ASKINGS = ('Whether to include 0-9? [Y/N] ', 'Whether to include a-z? [Y/N] ', 'Whether to include A-Z? [Y/N] ', 'Whether to include !@#$%^&* ? [Y/N] ')
INCLUDE = ('0123456789', 'abcdefghijklmnopqrstuvwxyz', 'ABCDEFGHIJKLMNOPQRSTUVWXYZ', '!@#$%^&*')
print('----\nPassword Generator\nVersion 2.2_23.08.05\nhttps://github.com/oniyukai/Password-Generator\n----')

while True:
    characters = ''
    length = int(input('\nInput the length of password: '))
    sets = int(input('Input several sets of generated passwords: '))
    for i in range(4):
        answer = input(ASKINGS[i])
        characters += INCLUDE[i] if answer=='Y' or answer=='y' else ''
    answer = input('Whether to input additions? [Y/N] ')
    characters += input('Input additions: ') if answer=='Y' or answer=='y' else ''
    print('\nGenerated password:')
    for _ in range(sets):
        print(''.join(random.choices(characters, k=length)))
