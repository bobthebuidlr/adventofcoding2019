import requests
import math

URL = 'https://adventofcode.com/2019/day/1/input'
cookies = {'_ga': 'GA1.2.358752375.1576073833', '_gid': 'GA1.2.1170832210.1576073833', 'session': '53616c7465645f5f5a1415f611dcf974128ee0284cb0a6fb1e295e2115705ae2898c586d5fee62756b6f3f931df67236'}

r = requests.get(URL, cookies=cookies)
data = r.content.decode('ascii')

with open('day1_input.txt', 'w') as f:
    f.write(data)


def calculate_fuel(mass):
    return math.floor(int(mass) / 3) - 2


with open('day1_input.txt', 'r') as f:
    total = 0
    for item in f:
        total += calculate_fuel(item)
    print(total)


