file = open('input.txt','r')
lines = file.readlines()

total_unique = len(lines)-1
total_cards = 0

card_results = []
for line in lines:
    split_line = line.split(': ')
    split_line = split_line[1].split(' | ')
    winning_number = split_line[0].split()
    your_numbers = split_line[1].split()

    current_points = 0

    for number in your_numbers:
        if number in winning_number:
            current_points += 1
    # adds the result to an array for easy lookup
    card_results.append([current_points,1])

index = 0
# go through all the card_results 
while index < len(card_results):
    print(card_results[index])
    total_cards += card_results[index][1]
    for i in range(1,card_results[index][0]+1):
        if index + i < len(card_results):
            card_results[index + i][1] += card_results[index][1]
    index += 1
print(total_cards)