file = open('input.txt','r')
lines = file.readlines()

i = 0
# adds horizontal galaxy expansion
while i < len(lines):
    lines[i] = lines[i].strip()
    if '#' not in lines[i]:
        lines[i] = 'M'*len(lines[i])
    i += 1

# Expands the universe vertically
i = 0
while i < len(lines[0]):
    # Gets all the characters in the vertical row
    vertical_row = []
    for j in range(len(lines)):
        vertical_row.append(lines[j][i])
    if '#' not in vertical_row:
        for j in range(len(lines)):
            if lines[j][i] == 'M':
                lines[j] = lines[j][:i] + 'B' + lines[j][i+1:]
            else:
                lines[j] = lines[j][:i] + 'M' + lines[j][i+1:]
        i += 2
    else:
        i += 1
    
galaxies = []
actual_rows = 0
for i in range(len(lines)):
    if ('.' not in lines[i]) and ('#' not in lines[i]):
        actual_rows += 1_000_000
        continue
    actual_col = 0
    for j in range(len(lines[i])):
        if lines[i][j] == 'M':
            actual_col += 1_000_000
            continue
        if lines[i][j] == '#':
            galaxies.append([actual_rows,actual_col])
        actual_col += 1
    actual_rows += 1

shortest_path_sum = 0
for i in range(len(galaxies)):
    for j in range(i+1,len(galaxies)):
        dx = abs(galaxies[i][0] - galaxies[j][0])
        dy = abs(galaxies[i][1] - galaxies[j][1])
        distance = dy + dx
        shortest_path_sum += distance

print(shortest_path_sum)