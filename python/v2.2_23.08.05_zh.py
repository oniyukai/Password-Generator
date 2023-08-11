import random

print('----\n密碼生成器\nVersion 2.2_23.08.05_zh\nhttps://github.com/oniyukai/Password-Generator\n----')
askings = ('是否要包含0-9? [Y/N] ', '是否要包含a-z? [Y/N] ', '是否要包含A-Z? [Y/N] ', '是否要包含「!@#$%^&*」? [Y/N] ')
include = ('0123456789', 'abcdefghijklmnopqrstuvwxyz', 'ABCDEFGHIJKLMNOPQRSTUVWXYZ', '!@#$%^&*')

while True:
    characters = ''
    length = input('\n輸入密碼生成幾組: ')
    sets = input('輸入密碼的長度: ')
    for i in range(4):
        answer = input(askings[i])
        characters += include[i] if answer=='Y' or answer=='y' else ''
    answer = input('是否要輸入額外字符？ [Y/N] ')
    characters += input('輸入額外的字符: ') if answer=='Y' or answer=='y' else ''
    print('生成的密碼:')
    for i in range(int(sets)):
        print(''.join(random.choices(characters, k=int(length))))
