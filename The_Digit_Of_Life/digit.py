#!/usr/bin/python3

state = True

while state:
    try:
        text = input('Please input your birthday in DDMMYYYY format: ')
        if len(text) == 8:
            text = int(text)
        else:
            raise exception('Input 8 digits...')
    except ValueError:
        print('Try again...')
    else:
        state = False

birthday = str(text)
sum = text
while True:
    if sum < 10:
        break
    birthday = str(sum)
    sum = 0
    for ch in birthday:
        sum += int(ch)
print(sum)
