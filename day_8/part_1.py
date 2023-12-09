file = open('input.txt','r')
lines = file.readlines()

instructions = lines[0].strip()
lines = lines[2:]

dictionary = {}
steps = 0
current_node = 'AAA'

for line in lines:
    parser = line.split()
    dictionary[parser[0]] = [parser[2][1:-1],parser[3][:-1]]

while current_node != 'ZZZ':
    next_step = dictionary[current_node]
    left_or_right = instructions[steps % len(instructions)]
    if left_or_right == 'L':
        current_node = next_step[0]
    else:
        current_node = next_step[1]
    steps += 1

print(steps)