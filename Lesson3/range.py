a = list(range(0, 12, 2))
b = list(range(15, 25, 3))
print(f'List A: {a}\nList B: {b}')

print([n for n in b if (n%2) ==0])