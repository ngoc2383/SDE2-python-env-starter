# How can we use loops to reduce the necessary code that does the following
presidents = ['Washington','Adams','Jefferson']

print('\n-----\n')
for i, president in enumerate(presidents):
    print((f"{president} was president #{i+1}"))

print('\n-----\n')
count = 0
while count < len(presidents):
    print((f"{presidents[count]} was president #{count+1}"))
    count += 1

print('\n-----\n')
for i in range(len(presidents)):
    print(f"{presidents[i]} was president #{i+1}")

print('\n-----\n')
[print(f"{president} was president #{i+1}") for i, president in enumerate(presidents)]

pres = 'Jefferson'
come_before = 0
for president in presidents:
    if president != pres:
        come_before += 1
    else:
        break
print(f'\n{come_before} presidents came before president {pres}')

'''
print(f"{presidents[0]} was president #1")
print(f"{presidents[1]} was president #2")
print(f"{presidents[2]} was president #3")
'''
# How do you get the index (the number between square brackets [])?
# What happens if we add a president to the list? What happens if we remove a president from the list?