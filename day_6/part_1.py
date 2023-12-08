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
    min_time = 0
    max_time = total_time
    for i in range(total_time):
        distance_traveled = (max_time-i) * i
        if distance_traveled > total_distance:
            min_time = i
            break
    for i in range(total_time,0,-1):
        distance_traveled = (max_time-i) * i
        if distance_traveled > total_distance:
            max_time = i
            break
    total_range *= (max_time-min_time) + 1
    index += 1
print(total_range)