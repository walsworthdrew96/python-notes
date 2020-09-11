from math import ceil, floor

population_size = 2903458039
number_of_districts = 38
districts = []
new_districts = []

total_remaining = number_of_districts

if total_remaining % 2 == 0:
    new_districts = []
    bulk = population_size // number_of_districts
    starting_remainder = population_size % number_of_districts

    print(f'bulk per district: {bulk}')
    print(f'remainder for all districts: {starting_remainder}')
    for x in range(number_of_districts):
        new_districts.append(population_size//number_of_districts)
    # print(f'new districts before: {new_districts}')

    count = 0
    remainder = starting_remainder
    while remainder > 0:
        cur_index = count % number_of_districts
        remainder -= 1
        new_districts[cur_index] += 1
        count += 1

    num_bulk_plus_1 = starting_remainder
    num_bulk = number_of_districts - starting_remainder
    # print(f'new districts after:  {new_districts}')
    print(f'new districts:  {new_districts}')

    print(f'{total_remaining} districts determined as {num_bulk} groups of {bulk} and {num_bulk_plus_1} groups of {bulk+1}, {0} population remaining')
else:
    while total_remaining > 0:
        half_number = total_remaining / 2
        ceil_val = ceil(half_number)
        floor_val = floor(half_number)
        print(f'{ceil_val}:{floor_val}', end='')
        if ceil_val % 2 == 1:
            print(f' -> {ceil_val} districts remaining, {floor_val} districts determined as groups of {population_size/number_of_districts}, {population_size/number_of_districts*ceil_val} population remaining')
            total_remaining = ceil_val
            if ceil_val == 1:
                break
        else:
            print(f' -> {floor_val} districts remaining, {ceil_val} districts determined as groups of {population_size/number_of_districts}, {population_size/number_of_districts*floor_val} population remaining')
            total_remaining = floor_val
            if floor_val == 1:
                break




