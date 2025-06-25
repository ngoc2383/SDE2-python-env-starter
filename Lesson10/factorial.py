def factorial(n):
    result = n
    current = n
    while current > 0:
        current =- 1
        result = result * current
    return result

def fac_recursive(n):
    if n == 0:
        return 1
    else:
        return n * fac_recursive(n-1)
    
print(fac_recursive(10))
print(fac_recursive(2))
print(fac_recursive(1))