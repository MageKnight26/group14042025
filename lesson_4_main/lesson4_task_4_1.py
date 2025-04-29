# input task list
numbers_list1 = [0, 1, 0, 12, 3]
numbers_list2 = [0]
numbers_list3 = [1, 0, 13, 0, 0, 0, 5]
numbers_list4 = [9, 0, 7, 31, 0, 45, 0, 45, 0, 45, 0, 0, 96, 0]
all_lists = [numbers_list1, numbers_list2, numbers_list3, numbers_list4]

for sublist in all_lists:  # processing each list separately
    original = sublist.copy()  # Copy for print "{original}..."
    result = []
    zero_counter = 0

    for num in sublist:
        if num != 0:
            result.append(num)
        else:
            zero_counter += 1

    result += [0] * zero_counter  # Add all zeros
    # Format output result
    print(f"{original} -> {result}")
