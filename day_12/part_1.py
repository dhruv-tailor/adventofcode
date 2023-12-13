file = open('test_input.txt','r')
lines = file.readlines()

condition_records = []
for line in lines:
    split_lines = line.split()
    condition_records.append([split_lines[0],split_lines[1].split(',')])

for condition in condition_records:
    print(condition)