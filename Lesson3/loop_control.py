presidents = ['Washington', 'Adams', 'Jefferson', 'Madison', 'Monroe', 'Adams']
see_next = 'y'
index = 0

while (index < len(presidents)) and (see_next == 'y'):
    print(f'{presidents[index]} was president #{index+1}')
    see_next = input('Do you wanna see the next president (y/ n): ')
    if see_next == 'n' or see_next == 'no':
        break
    index += 1

print(f'You just saw the first {index+1} presidents')
