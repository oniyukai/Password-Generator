import random

print ('--------------------\n密碼生成器 Version 2.2_2022.06.19\nMade by YU KAI\n--------------------')
announcement = ["是否要加入1-9？ [Y/N] ", "是否要加入a-z？ [Y/N] ", "是否要加入A-Z？ [Y/N] ", "是否要加入「!@#$\%^&*」？ [Y/N] ", "是否要輸入而外字符？ [Y/N] ", "輸入而外字符: ", "\n輸入密碼的長度: ", "輸入生成幾組密碼: ", "生成的密碼:"]
character = ["0123456789", "abcdefghijklmnopqrstuvwxyz", "ABCDEFGHIJKLMNOPQRSTUVWXYZ", "!@#$%^&*"]
while True:
    data = ""
    long = input(announcement[6])
    groups = input(announcement[7])
    for n in range(4):
        answer = input(announcement[n])
        if answer == "Y" or answer == "y":
            data += character[n]
    answer = input(announcement[4])
    if answer == "Y" or answer == "y":
        answer = input(announcement[5])
        data += answer
    print(announcement[8])
    for groups in range(int(groups)):
        password = ''.join(random.choices(data, k = int(long)))
        print(password)