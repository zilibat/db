import json
from os import times

with open('./data.json', 'r') as file:
    data = json.load(file)

name = input()
time = input()
seek = []

for order in data['db']['orders']:
    if order['client']['name'] == name and order['time'] == time:
        seek.append(order)
print(seek)