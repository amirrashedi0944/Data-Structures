# Recursive relationship ---> f(n) = f(n-1) + 1 + f(n-1) = 2f(n-1) + 1
def end_of_universe(numberOfRings):
    if numberOfRings == 1:
        return 1
    else:
        return 2*end_of_universe(numberOfRings-1) + 1


lifetimeOfUniverse = end_of_universe(64) / (3600 * 24 * 365 * 1_000_000_000)
print(f'Lifetime of universe is {lifetimeOfUniverse} billion years.' )
