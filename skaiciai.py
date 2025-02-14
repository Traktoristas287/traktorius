def natural_numbers_sum(n):
    return n * (n + 1) // 2

# Patikrinkime skaičius 55 ir 66
numbers_to_check = [55, 66]

for number in numbers_to_check:
    for n in range(1, number + 1):
        if natural_numbers_sum(n) == number:
            print(f"{number} = suma nuo 1 iki {n}")
            break
