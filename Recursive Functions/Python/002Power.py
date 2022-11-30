def power(base, exponent):
    if exponent == 0:
        return 1
    else:
        return base * pow(base, exponent - 1)


base = int(input("Enter the base number: "))
exponent = int(input("Enter the power: "))
print(f'{base}^{exponent} = {pow(base, exponent)}')
