def sumEven(number):
    if number == 2:
        return 2
    elif number % 2 == 0:
        return number + sumEven(number - 2)
    else:
        return sumEven(number - 1)


number = int(input("Enter the number: "))
print(f'The sum of even numbers from 1 to {number} is {sumEven(number)}.')
