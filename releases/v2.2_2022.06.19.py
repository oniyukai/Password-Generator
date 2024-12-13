import random

print ('--------------------\nPassword Generator Version 2.2_2022.06.19\nMade by YU KAI\n--------------------')
announcement = ["Whether to add 1-9? [Y/N] ", "Whether to add a-z? [Y/N] ", "Whether to add A-Z? [Y/N] ", "Whether to add \"!@#$\%^&*\"? [Y/N] ", "Whether to enter characters outside? [Y/N] ", "Enter the outer characters: ", "\nEnter the length of the password: ", "Enter several sets of generated passwords: ", "Generated password:"]
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