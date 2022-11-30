def sumOfDigits(number):
    if number // 10 == 0:
        return number
    else:
        return (number % 10) + sumOfDigits(number // 10)


number = int(input("Enter the number: "))
print(f'Sum of digits = {sumOfDigits(number)}')
