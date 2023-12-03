import re
lines = open('input.txt', 'r').readlines()
total = 0

for index, line in enumerate(lines):
    numbers = re.finditer(r'\d+', line)
    for number in numbers:
        y = [max(index-1, 0), min(index+2, len(lines)-1)]
        x = [max(number.start()-1, 0), min(number.end()+1, len(line)-1)]

        stringsToCheck = [k[x[0]:x[1]] for k in lines[y[0]:y[1]]]
        for stringToCheck in stringsToCheck:
            if re.search(r'[^\d.]', stringToCheck):
                total += int(number.group())
                break
print(total)
