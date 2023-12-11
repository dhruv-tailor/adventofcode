file = open('input.txt','r')
lines = file.readlines()

prediction_total = 0

for line in lines:
    orignal_numbers = line.split()
    converted_numbers = [int(number) for number in orignal_numbers]
    last_number_stack = [converted_numbers[-1]]
    while not all(number == 0 for number in converted_numbers):
        change_in_numbers = []
        for i in range(len(converted_numbers)-1):
            change_in_numbers.append(converted_numbers[i+1]-converted_numbers[i])
        last_number_stack.append(change_in_numbers[-1])
        converted_numbers = change_in_numbers
    prediction = sum(last_number_stack)
    prediction_total += prediction

print(prediction_total)