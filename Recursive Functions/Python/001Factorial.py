def facturial(number):
    if number == 0:
        return 1
    else:
        return number * facturial(number - 1)


number = int(input("Enter a number: "))
print(f'{number}! ={facturial(number)}')
