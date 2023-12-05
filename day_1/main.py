file = open('input.txt','r')
lines = file.readlines()
first_digit = 0
last_digit = 0
total = 0
text_to_number = [['one','o1e'],['two','t2o'],['three','t3e'],['four','f4'],['five','f5e'],['six','s6'],['seven','s7n'],['eight','e8t'],['nine','n9e']]
# iterate on every line in the input
for line in lines:
    for digit in text_to_number:
        line = line.replace(digit[0],digit[1])
    # get the first number
    for character in line:
        if character.isdigit():
            first_digit = int(character) * 10
            break
    # get the last number
    for character in reversed(line):
        if character.isdigit():
            last_digit = int(character)
            break
    total = total + first_digit + last_digit
print(total)