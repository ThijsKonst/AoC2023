lines = open('input.txt', 'r').readlines()
sum = 0
for line in lines:
    output = ""
    for char in line:
        if char.isdigit():
            output += char
    answer = output[0] + output[-1]
    sum += int(answer)

print(sum)
