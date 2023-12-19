parts = open('input.txt', 'r').read().split()[0].split(',')

boxes = [{} for x in range(256)]


def hash(input):
    current = 0
    for char in input:
        current += ord(char)
        current *= 17
        current %= 256
    return current


for part in parts:
    if '-' in part:
        boxes[hash(part[:-1])].pop(part[:-1], 0)
        continue
    label, amount = part.split('=')
    boxes[hash(label)][label] = amount

total = 0
for index, box in enumerate(boxes):
    for slot, v in enumerate(box.values()):
        total += (slot+1)*(index+1)*int(v)
print(total)
