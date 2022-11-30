def summation(n):
    if n == 1:
        return 1
    else:
        return n + summation(n-1)


number = int(input("Enter a number: "))
print(f'sum = {summation(number)}')
