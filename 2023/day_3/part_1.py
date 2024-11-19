file = open('input.txt','r')
lines = file.readlines()
total_sum = 0
current_x = 0
for line in lines:
    digits = []
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
            total_sum += current_number
            digits = []
        elif getting_number:
            digits = []
            getting_number = False
            symbol_adjacent = False
        
        # looks to find any touching symbol
        if getting_number and not symbol_adjacent:
            for x in range(-1,2):
                # makes sure you're not trying to find something out of bounds
                if ((current_x + x) < 0) or ((current_x + x) >= len(line)):
                    continue
                for y in range(-1,2):
                    if ((current_y + y) < 0) or ((current_y + y) >= len(lines)):
                        continue
                    if (not lines[current_x + x][current_y + y].isdigit()) and (not lines[current_x + x][current_y + y] == '.'):
                        symbol_adjacent = True

        current_y += 1
    current_x += 1
print(total_sum)