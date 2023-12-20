lines = [(x.split()[0], int(x.split()[1]), x.split()[2][1:-1])
    for x in open('input.txt', 'r').readlines()]

current = (0, 0)
convert = {
    0: (0, 1),
    1: (1, 0),
    2: (0, -1),
    3: (-1, 0),
}
coords = []

def moveThrough(coords):
    #A function to apply the Shoelace algorithm
    numberOfVertices = len(coords)
    sum1 = 0
    sum2 = 0
  
    for i in range(0,numberOfVertices-1):
        sum1 += coords[i][0] *  coords[i+1][1]
        sum2 += coords[i][1] *  coords[i+1][0]
    
    #Add xn.y1
    sum1 = sum1 + coords[numberOfVertices-1][0]*coords[0][1]   
    #Add x1.yn
    sum2 = sum2 + coords[0][0]*coords[numberOfVertices-1][1]   
    
    area = abs(sum1 - sum2) / 2
    return area


def normalize(coords):
    rowLowerBound = min([x[0] for x in coords])
    colLowerBound = min([x[1] for x in coords])
    return [(x-rowLowerBound, y-colLowerBound) for x, y in coords]

corners = []
total = 0
for direction, amount, color in lines:
    amount, direction = int(color[1:-1], 16), int(color[-1])
    total += amount

    mutation = (amount * convert[direction][0], amount * convert[direction][1])
    
    current = tuple(map(sum, zip(current, mutation)))
    corners.append(current)

corners = normalize(corners)
print(moveThrough(corners) + total/2 +1)
