import numpy as np

file = open('input.txt','r')
lines = file.readlines()

instructions = lines[0].strip()
lines = lines[2:]

dictionary = {}

ghosts = []
ghost_steps = []

for line in lines:
    parser = line.split()
    dictionary[parser[0]] = [parser[2][1:-1],parser[3][:-1]]

for k,v in dictionary.items():
    if k[-1] == 'A':
        ghosts.append(k)

for i in range(len(ghosts)):
    ghost_steps.append(0)
    while ghosts[i][-1] != 'Z':
        next_step = dictionary[ghosts[i]]
        left_or_right = instructions[ghost_steps[-1] % len(instructions)]
        if left_or_right == 'L':
            ghosts[i] = next_step[0]
        else:
            ghosts[i] = next_step[1]
        ghost_steps[-1] += 1

print(np.lcm.reduce(ghost_steps))