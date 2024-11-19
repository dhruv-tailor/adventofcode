max_red = 12
max_green = 13
max_blue = 14

file = open('input.txt','r')
lines = file.readlines()
id_sum = 0

for line in lines:
    # get the game ID
    new_line = line.split(': ')
    game_id = int(new_line[0].split()[1])
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

    games_viable = True
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
        # if a hand is found impossible the game breaks
        if (green_value > max_green) or (red_value > max_red) or (blue_value > max_blue):
            games_viable = False
            break

    if games_viable:
        id_sum += game_id
print(id_sum)