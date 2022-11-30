def fibo(n):
    if n == 1:
        return 1
    elif n== 2:
        return 1
    else:
        return fibo(n-1) + fibo(n-2)


n = int(input("Enter the nth sentence of the sequence : "))
print(f'{n}th sentence = {fibo(n)}')
