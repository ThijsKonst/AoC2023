import re
lines = open('input.txt', 'r').readlines()
total = 0
gears = {}

for index, line in enumerate(lines):
    numbers = re.finditer(r'\d+', line)
    for number in numbers:
        y = [max(index-1, 0), min(index+2, len(lines))]
        x = [max(number.start()-1, 0), min(number.end()+1, len(line)-1)]

        stringsToCheck = [k[x[0]:x[1]] for k in lines[y[0]:y[1]]]
        for pils, stringToCheck in enumerate(stringsToCheck):
            bier = stringToCheck.find('*')
            if bier >= 0:
                location = (y[0]+pils, x[0] + bier)
                if location in gears.keys():
                    total += int(number.group()) * gears[location]
                    break
                gears[location] = int(number.group())
print(total)
