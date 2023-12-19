parts = open('input.txt', 'r').read().split()[0].split(',')

total = 0
for part in parts:
    current = 0
    for char in part:
        current += ord(char)
        current *= 17
        current %= 256
    total += current
print(total)
