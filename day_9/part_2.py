file = open('input.txt','r')
lines = file.readlines()

prediction_total = 0

for line in lines:
    orignal_numbers = line.split()
    converted_numbers = [int(number) for number in orignal_numbers]
    first_number_stack = [converted_numbers[0]]
    while not all(number == 0 for number in converted_numbers):
        change_in_numbers = []
        for i in range(len(converted_numbers)-1):
            change_in_numbers.append(converted_numbers[i+1]-converted_numbers[i])
        first_number_stack.append(change_in_numbers[0])
        converted_numbers = change_in_numbers

    while len(first_number_stack) > 1:
        last_number = first_number_stack.pop()
        second_last_number = first_number_stack.pop()
        difference = second_last_number - last_number
        first_number_stack.append(difference)
    prediction = first_number_stack[0]
    prediction_total += prediction
print(prediction_total)