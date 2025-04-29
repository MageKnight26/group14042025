# Input task
numbers_list1 = [0, 1, 7, 2, 4, 8]
numbers_list2 = [1, 3, 5]
numbers_list3 = [6]
numbers_list4 = []
all_lists = [numbers_list1, numbers_list2, numbers_list3, numbers_list4]
for sublist in all_lists:  # processing each list
    if not sublist:
        print(f"{sublist} -> 0")
        continue
    sum_even_index = 0
    for index in range(0, len(sublist), 2):  # we only go through paired index
        sum_even_index += sublist[index]
    result = sum_even_index * sublist[-1]  # multiply by the last element of the list
    print(f"{sublist} => {result}")
