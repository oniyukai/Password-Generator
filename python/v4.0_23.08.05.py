import random

ASKINGS = ('Whether to include 0-9? [Y/N] ', 'Whether to include a-z? [Y/N] ', 'Whether to include A-Z? [Y/N] ', 'Whether to include !@#$%^&* ? [Y/N] ')
INCLUDE = ('0123456789', 'abcdefghijklmnopqrstuvwxyz', 'ABCDEFGHIJKLMNOPQRSTUVWXYZ', '!@#$%^&*')
MAX_SECTION = 4
print('----\nPassword Generator\nVersion 4.0_23.08.05\nhttps://github.com/oniyukai/Password-Generator\n----')

while True:
    sets = int(input('\n\nInput several sets of generated passwords: '))
    sections = int(input(f'Input the several sections of the password (Up to {MAX_SECTION} sections): '))
    while sections > MAX_SECTION or sections < 1:
        sections = int(input('Error, please input another response again: '))
    sections = [''] * sections
    sections_length = []
    for i in range(len(sections)):
        print(f'\nSetting the {i+1}/{len(sections)} section:')
        sections_length.append(int(input('Input the length of this section: ')))
        for j in range(4):
            answer = input(ASKINGS[j])
            sections[i] += INCLUDE[j] if answer=='Y' or answer=='y' else ''
        answer = input('Whether to input additions? [Y/N] ')
        sections[i] += input('Input additions: ') if answer=='Y' or answer=='y' else ''
    print('\nGenerated password:')
    for _ in range(sets):
        for i in range(len(sections)):
            print(''.join(random.choices(sections[i], k=sections_length[i])), end='')
        print()
