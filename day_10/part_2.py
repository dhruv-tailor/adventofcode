file = open('test_input_3.txt','r')
lines = file.readlines()

# The trick is to check all values to the left and right and see if there's an odd number of pipes
# Find starting position
previous_position = [0,0]
current_position = [0,0]
boundries = []
for i in range(len(lines)):
    if 'S' in lines[i]:
        current_position[0] = i
        current_position[1] = lines[i].index('S')
        previous_position = [current_position[0],current_position[1]]
        break

loop_length = 0

# | is a vertical pipe connecting north and south.
# - is a horizontal pipe connecting east and west.
# L is a 90-degree bend connecting north and east.
# J is a 90-degree bend connecting north and west.
# 7 is a 90-degree bend connecting south and west.
# F is a 90-degree bend connecting south and east.
# . is ground; there is no pipe in this tile.
# S is the starting position of the animal; there is a pipe on this tile, but your sketch doesn't show what shape the pipe has.

# Calculate the boundries
while True:
    current_position.append([current_position[0],current_position[1]])
    boundries.append([current_position[0],current_position[1]])
    # Check if we are in the starting position
    if lines[current_position[0]][current_position[1]] == 'S':
        # Check above
        if (lines[current_position[0]-1][current_position[1]] == '|') or (lines[current_position[0]-1][current_position[1]] == '7') or (lines[current_position[0]-1][current_position[1]] == 'F'):
            current_position[0] -= 1
            loop_length += 1
        # Check below
        elif (lines[current_position[0]+1][current_position[1]] == '|') or (lines[current_position[0]+1][current_position[1]] == 'L') or (lines[current_position[0]+1][current_position[1]] == 'J'):
            current_position[0] += 1
            loop_length += 1
        # Check left
        elif (lines[current_position[0]][current_position[1]-1] == '-') or (lines[current_position[0]][current_position[1]-1] == 'L') or (lines[current_position[0]][current_position[1]-1] == 'F'):
            current_position[1] -= 1
            loop_length += 1
        # Check right
        elif (lines[current_position[0]][current_position[1]+1] == '-') or (lines[current_position[0]][current_position[1]+1] == '7') or (lines[current_position[0]][current_position[1]+1] == 'J'):
            current_position[1] += 1
            loop_length += 1
    # check for vertical pipe
    elif lines[current_position[0]][current_position[1]] == '|':
        # Check above
        if ([current_position[0]-1,current_position[1]] != previous_position):
            previous_position = [current_position[0],current_position[1]]
            current_position[0] -= 1
            loop_length += 1
        else:
            previous_position = [current_position[0],current_position[1]]
            current_position[0] += 1
            loop_length += 1
    # check for horizontal pipe
    elif lines[current_position[0]][current_position[1]] == '-':
        # Check left
        if ([current_position[0],current_position[1]-1] != previous_position):
            previous_position = [current_position[0],current_position[1]]
            current_position[1] -= 1
            loop_length += 1
        else:
            previous_position = [current_position[0],current_position[1]]
            current_position[1] += 1
            loop_length += 1
    # check for L
    elif lines[current_position[0]][current_position[1]] == 'L':
        # Check above
        if ([current_position[0]-1,current_position[1]] != previous_position):
            previous_position = [current_position[0],current_position[1]]
            current_position[0] -= 1
            loop_length += 1
        # Check Right
        else:
            previous_position = [current_position[0],current_position[1]]
            current_position[1] += 1
            loop_length += 1
    # check for J
    elif lines[current_position[0]][current_position[1]] == 'J':
        # Check above
        if ([current_position[0]-1,current_position[1]] != previous_position):
            previous_position = [current_position[0],current_position[1]]
            current_position[0] -= 1
            loop_length += 1
        # Check Left
        else:
            previous_position = [current_position[0],current_position[1]]
            current_position[1] -= 1
            loop_length += 1
    # check for 7
    elif lines[current_position[0]][current_position[1]] == '7':
        # Check below
        if ([current_position[0]+1,current_position[1]] != previous_position):
            previous_position = [current_position[0],current_position[1]]
            current_position[0] += 1
            loop_length += 1
        # Check Left
        else:
            previous_position = [current_position[0],current_position[1]]
            current_position[1] -= 1
            loop_length += 1
    # check for F
    elif lines[current_position[0]][current_position[1]] == 'F':
        # Check below
        if ([current_position[0]+1,current_position[1]] != previous_position):
            previous_position = [current_position[0],current_position[1]]
            current_position[0] += 1
            loop_length += 1
        # Check Right
        else:
            previous_position = [current_position[0],current_position[1]]
            current_position[1] += 1
            loop_length += 1
    if lines[current_position[0]][current_position[1]] == 'S':
        break

# total dots in area
total_dots = 0
dot_locations = []

# Calculate to see if dot is within boundries
for i in range(len(lines)):
    for j in range(len(lines[i])):
        # Check if dot
        if lines[i][j] == '.':
            # fire a ray to the left
            parity = 0
            for k in range(j+1,len(lines[i])):
                if [i,k] in boundries and lines[i][k] not in ['L','7']:
                    parity += 1            
            if parity % 2 == 1:
                total_dots += 1
                dot_locations.append([i,j])

print(dot_locations)
print(total_dots)
                