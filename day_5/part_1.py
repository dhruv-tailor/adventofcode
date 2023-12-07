file = open('input.txt','r')
lines = file.readlines()

# Get the vaules of all the seeds
seeds = lines.pop(0).split()[1:]
for i in range(len(seeds)):
    seeds[i] = int(seeds[i])

lines.pop(0)
lines.pop(0)

# get the mapping values for all steps
paths = [[]]
for line in lines:
    if line == '\n':
        paths.append([])
    elif ':' not in line:
        number_list = line.split()
        for i in range(len(number_list)):
            number_list[i] = int(number_list[i])
        paths[-1].append(number_list)

# Calculate Values for seeds
for map in paths:
    for i, seed in enumerate(seeds):
        for gen_alg in map:
            if (seed >= gen_alg[1]) and (seed < gen_alg[1]+gen_alg[2]):
                seeds[i] = gen_alg[0] + (seed - gen_alg[1])
                break
seeds.sort()
print(seeds[0])