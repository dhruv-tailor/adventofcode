import math


file = open('input.txt','r')
lines = file.readlines()

times = lines[0].split()[1:]
distances = lines[1].split()[1:]

total_time = ''
total_distance = ''

for time in times:
    total_time += time

for distance in distances:  
    total_distance += distance

total_time = int(total_time)
total_distance = int(total_distance)

total_range = 1

determinant = math.sqrt((total_time**2) - (4*total_distance))
plus_values = int(((-1 * total_time) + determinant) / (-2))
minus_values = int(((-1 * total_time) - determinant) / (-2))

print(minus_values - plus_values)