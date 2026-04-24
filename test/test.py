import random

key_sequence = []

keys = [
    'up',
    'down',
    'left',
    'right',
    'x',
    'z'
]

for i in range(0, 100):
    key_sequence.append(random.choice(keys))
    print(key_sequence[i])