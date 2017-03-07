import math

distance = 0
width = 2
for r in range(0, width):
    for c in range(0, width):
        distance += math.sqrt(r**2+c**2)

print(distance)