def sumOdd(number):
    if number == 1:
        return 1
    elif number % 2 == 1:
        return number + sumOdd(number - 2)
    else:
        return sumOdd(number - 1)

number = int(input("Enter the number : "))
print(f'The sum of odd numbers from 1 to {number} is {sumOdd(number)}.')
