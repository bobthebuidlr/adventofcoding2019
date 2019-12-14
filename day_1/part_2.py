import math


def calculate_fuel(mass):
    needed_fuel = math.floor(int(mass) / 3) - 2

    # Add the needed fuel to the array
    if needed_fuel > 0:
        fuel_costs[i] += needed_fuel
        calculate_fuel(needed_fuel)

    # Stop calculation for the initial mass
    else:
        return


with open('input.txt', 'r') as f:
    # Initialize an array to store the fuel costs
    fuel_costs = [0] * 100

    for i, mass in enumerate(f):
        calculate_fuel(mass)

    # Print out the sum of fuel costs
    print(sum(fuel_costs))
