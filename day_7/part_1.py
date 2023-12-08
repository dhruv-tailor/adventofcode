file = open('input.txt','r')
lines = file.readlines()

card_values = ['A','K','Q','J','T','9','8','7','6','5','4','3','2']

five_of_a_kind = []
four_of_a_kind = []
full_house = []
three_of_a_kind = []
two_pair = []
one_pair = []
high_card = []

rank = len(lines)
total_score = 0

for line in lines:
    split_line = line.split()
    hand = split_line[0]
    hand = hand.replace('A','B')
    hand = hand.replace('K','C')
    hand = hand.replace('Q','D')
    hand = hand.replace('J','E')
    hand = hand.replace('T','F')
    hand = hand.replace('9','G')
    hand = hand.replace('8','H')
    hand = hand.replace('7','I')
    hand = hand.replace('6','J')
    hand = hand.replace('5','K')
    hand = hand.replace('4','L')
    hand = hand.replace('3','M')
    hand = hand.replace('2','N')
    value = int(split_line[1])
    sorted_hand = sorted(hand)
    # check for five of a kind.
    if hand[0] == hand[1] == hand[2] == hand[3] == hand[4]:
        five_of_a_kind.append((hand,value))
    # check for four of a kind
    elif (sorted_hand[0] == sorted_hand[1] == sorted_hand[2] == sorted_hand[3]) or (sorted_hand[1] == sorted_hand[2] == sorted_hand[3] == sorted_hand[4]):
        four_of_a_kind.append((hand,value))
    # check for full house
    elif ((sorted_hand[0] == sorted_hand[1] == sorted_hand[2]) and (sorted_hand[3] == sorted_hand[4])) or ((sorted_hand[4] == sorted_hand[3] == sorted_hand[2]) and (sorted_hand[1] == sorted_hand[0])):
        full_house.append((hand,value))
    # check for three of a kind
    elif (sorted_hand[0] == sorted_hand[1] == sorted_hand[2]) or (sorted_hand[1] == sorted_hand[2] == sorted_hand[3]) or (sorted_hand[2] == sorted_hand[3] == sorted_hand[4]):
        three_of_a_kind.append((hand,value))
    # check for two pair
    elif ((sorted_hand[0] == sorted_hand[1]) and (sorted_hand[2] == sorted_hand[3])) or ((sorted_hand[0] == sorted_hand[1]) and (sorted_hand[3] == sorted_hand[4])) or ((sorted_hand[1] == sorted_hand[2]) and (sorted_hand[3] == sorted_hand[4])):
        two_pair.append((hand,value))
    # check for one pair
    elif (sorted_hand[0] == sorted_hand[1]) or (sorted_hand[1] == sorted_hand[2]) or (sorted_hand[2] == sorted_hand[3]) or (sorted_hand[3] == sorted_hand[4]):
        one_pair.append((hand,value))
    # check for high card
    else:
        high_card.append((hand,value))

# sort the lists
five_of_a_kind.sort(key=lambda x: x[0])
four_of_a_kind.sort(key=lambda x: x[0])
full_house.sort(key=lambda x: x[0])
three_of_a_kind.sort(key=lambda x: x[0])
two_pair.sort(key=lambda x: x[0])
one_pair.sort(key=lambda x: x[0])
high_card.sort(key=lambda x: x[0])

for hand in five_of_a_kind:
    total_score += rank * hand[1]
    rank -= 1
for hand in four_of_a_kind:
    total_score += rank * hand[1]
    rank -= 1
for hand in full_house:
    total_score += rank * hand[1]
    rank -= 1
for hand in three_of_a_kind:
    total_score += rank * hand[1]
    rank -= 1
for hand in two_pair:
    total_score += rank * hand[1]
    rank -= 1
for hand in one_pair:
    total_score += rank * hand[1]
    rank -= 1
for hand in high_card:
    total_score += rank * hand[1]
    rank -= 1

print(total_score)