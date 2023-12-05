max_red = 12
max_green = 13
max_blue = 14

file = open('input.txt','r')
lines = file.readlines()
total_power = 0

for line in lines:
    # get the game ID
    new_line = line.split(': ')
    games = new_line[1].split('; ')
    split_games = []
    # Splits the list of games into individual games
    for game in games:
        scores = game.split(', ')
        split_scores = []
        # splits the game up by colors
        for score in scores:
            split_scores.append(score.split())
        split_games.append(split_scores)

    min_red = 0
    min_green = 0
    min_blue = 0
    for game in split_games:
        # get the individual values for each color
        green_value = 0
        red_value = 0
        blue_value = 0
        for color in game:
            if color[1] == 'green':
                green_value += int(color[0])
            elif color[1] == 'blue':
                blue_value += int(color[0])
            elif color[1] == 'red':
                red_value += int(color[0])
        # updates values to the mininum number of marbles needed
        if green_value > min_green:
            min_green = green_value
        if red_value > min_red:
            min_red = red_value
        if blue_value > min_blue:
            min_blue = blue_value

    power = min_red * min_blue * min_green
    total_power += power

print(total_power)