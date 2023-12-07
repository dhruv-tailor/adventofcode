import math


file = open('input.txt','r')
lines = file.readlines()

times = lines[0].split()[1:]
distances = lines[1].split()[1:]

total_range = 1

index = 0
while index < len(times):
    total_time = int(times[index])
    total_distance = int(distances[index])
    determinant = math.sqrt((total_time*total_time) - (4 * total_distance))
    plus_value = math.floor((total_time + determinant)/2)
    minus_value = math.ceil((total_time - determinant)/2)
    total_range *= (plus_value - minus_value)
    print(plus_value,minus_value)
    index += 1

print(total_range)