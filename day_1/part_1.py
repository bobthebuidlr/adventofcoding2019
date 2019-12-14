import math


def calculate_fuel(mass):
    return math.floor(int(mass) / 3) - 2


with open('input.txt', 'r') as f:
    total = 0
    for mass in f:
        total += calculate_fuel(mass)
    print(total)


