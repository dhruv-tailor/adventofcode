file = open('input.txt','r')
lines = file.readlines()

total_points = 0

for line in lines:
    split_line = line.split(': ')
    split_line = split_line[1].split(' | ')
    winning_number = split_line[0].split()
    your_numbers = split_line[1].split()

    current_points = 0

    for number in your_numbers:
        if number in winning_number:
            if current_points == 0:
                current_points += 1
            else:
                current_points *= 2

    total_points += current_points
print(total_points)