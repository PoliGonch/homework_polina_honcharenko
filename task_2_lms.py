def merge(left_list, right_list):
    sorted_list = []
    left_list_index = right_list_index = 0

    left_list_length, right_list_length = len(left_list), len(right_list)

    for _ in range(left_list_length + right_list_length):
        if left_list_index < left_list_length and right_list_index < right_list_length:
            if left_list[left_list_index] <= right_list[right_list_index]:
                sorted_list.append(left_list[left_list_index])
                left_list_index += 1

            else:
                sorted_list.append(right_list[right_list_index])
                right_list_index += 1

        elif left_list_index == left_list_length:
            sorted_list.append(right_list[right_list_index])
            right_list_index += 1

        elif right_list_index == right_list_length:
            sorted_list.append(left_list[left_list_index])
            left_list_index += 1

    return sorted_list


def merge_sort(nums):
    new_list = [[nums[i]] for i in range(len(nums))]
    new_num = merge(new_list[0], new_list[1])

    for i in range(2, len(nums)):
        new_num = merge(new_num, new_list[i])

    return new_num


random_list_of_nums = [5, 120, 45, 68, 250, 176, 1, 0, 17, 984]
# print(random_list_of_nums)
random_list_of_nums = merge_sort(random_list_of_nums)
print(random_list_of_nums)
