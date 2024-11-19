file = open('input.txt','r')
lines = file.readlines()

# Get the vaules of all the seeds
seeds = lines.pop(0).split()[1:]
for i in range(len(seeds)):
    seeds[i] = int(seeds[i])

seed_ranges = []
while seeds != []:
    start = seeds.pop(0)
    seed_range = seeds.pop(0)
    seed_ranges.append([start,start+seed_range-1])

lines.pop(0)
lines.pop(0)
print(seed_ranges)

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

for path in paths:
    print(path)

# Calculate Values for seeds
for map in paths:
    next_seed_turn = []
    for i, seed in enumerate(seed_ranges):
        unused_seed_ranges = [seed]
        while unused_seed_ranges != []:
            unused_seed_range = unused_seed_ranges.pop(0)
            # All these indecies are making my brain hurt
            for gen_alg in map:
                # if range contains the entire unused seed range
                if (gen_alg[1] <= unused_seed_range[0]) and ((gen_alg[1] + gen_alg[2]) > unused_seed_range[1]):
                    new_start = unused_seed_range[0]-gen_alg[1]+gen_alg[0]
                    new_end = unused_seed_range[1]-gen_alg[1]+gen_alg[0]
                    updated_range = [new_start,new_end]
                    unused_seed_range = []
                    next_seed_turn.append(updated_range)
                    break
                # if the seed range contains the map range
                elif (unused_seed_range[0] <= gen_alg[1]) and (unused_seed_range[1] >= (gen_alg[1] + gen_alg[2])):
                    unused_seed_ranges.append([unused_seed_range[0],gen_alg[1]-1])
                    unused_seed_ranges.append([(gen_alg[1] + gen_alg[2]),unused_seed_range[1]])
                    new_start = gen_alg[0]
                    new_end = gen_alg[0] + gen_alg[2] - 1
                    updated_range = [new_start,new_end]
                    next_seed_turn.append(updated_range)
                # Range is left half
                elif (unused_seed_range[0] >= gen_alg[1]) and (unused_seed_range[0] <= (gen_alg[1] + gen_alg[2])) and ((gen_alg[1] + gen_alg[2]) <= unused_seed_range[1]):
                    unused_seed_ranges.append([(gen_alg[1] + gen_alg[2]),unused_seed_range[1]])
                    new_start = gen_alg[0] + (unused_seed_range[1] - gen_alg[1])
                    new_end = gen_alg[0] + gen_alg[2]
                    updated_range = [new_start,new_end]
                    next_seed_turn.append(updated_range)
                # Range is Right Half
