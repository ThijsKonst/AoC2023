lines = open('input.txt', 'r').readlines()
conversion = ['one', 'two', 'three', 'four',
              'five', 'six', 'seven', 'eight', 'nine']
sum = 0
for line in lines:
    for index, number in enumerate(conversion):
        line = line.replace(number, number + str(index+1) + number)
    output = ""
    for char in line:
        if char.isdigit():
            output += char
    answer = output[0] + output[-1]
    sum += int(answer)

print(sum)
