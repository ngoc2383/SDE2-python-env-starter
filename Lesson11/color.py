red = '31'
blue = '34'
green = '32'
def letter(l, color):
    print('\033[' + color + 'm' + l + '\033[0m')

letter('Hello Word', red)