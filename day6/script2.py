time, distance = (int("".join(x.split()[1:]))
                  for x in open('input.txt', 'r').readlines())

sum = 1

sum *= len([(x, x * (time-x))
            for x in range(time) if x * (time-x) > distance])
print(sum)
