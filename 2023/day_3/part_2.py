file = open('input.txt','r')
lines = file.readlines()
total_sum = 0
current_x = 0
gear_dict = {}
for line in lines:
    digits = []
    gear_location = ''
    current_y = 0
    getting_number = False
    symbol_adjacent = False
    for char in line:
        # flags that a number has been found
        if char.isdigit():
            getting_number = True
            digits.append(int(char))
        elif getting_number and symbol_adjacent:
            getting_number = False
            symbol_adjacent = False
            current_number = 0
            current_power = 1
            for digit in reversed(digits):
                current_number += digit * current_power
                current_power *= 10
            if not (gear_location in gear_dict):
                gear_dict[gear_location] = []
            gear_dict[gear_location].append(current_number)
            gear_location = ''
            digits = []
        elif getting_number:
            digits = []
            getting_number = False
            symbol_adjacent = False
        
        # looks to find any touching gears
        if getting_number and not symbol_adjacent:
            for x in range(-1,2):
                # makes sure you're not trying to find something out of bounds
                if ((current_x + x) < 0) or ((current_x + x) >= len(line)):
                    continue
                for y in range(-1,2):
                    if ((current_y + y) < 0) or ((current_y + y) >= len(lines)):
                        continue
                    if lines[current_x + x][current_y + y] == '*':
                        symbol_adjacent = True
                        x_cord = current_x + x
                        y_cord = current_y + y
                        gear_location = str(x_cord) + ',' + str(y_cord)

        current_y += 1
    current_x += 1

for key, value in gear_dict.items():
    if len(value) > 1:
        total_sum += value[0] * value[1]

print(total_sum)