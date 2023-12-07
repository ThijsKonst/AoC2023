lines = list(zip(*[[int(y) for y in x.split()[1:]]
                   for x in open('input.txt', 'r').readlines()]))
sum = 1

for time, distance in lines:
    sum *= len([(x, x * (time-x))
                for x in range(time) if x * (time-x) > distance])
print(sum)
