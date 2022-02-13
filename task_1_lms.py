def bubble_sort_2_ways(list_to_sort: list[int]) -> list[int]:
    swapped = True
    start_index = 0
    end_index = len(list_to_sort) - 1

    while swapped:
        swapped = False

        for i in range(start_index, end_index):
            if list_to_sort[i] > list_to_sort[i + 1]:
                list_to_sort[i], list_to_sort[i + 1] = list_to_sort[i + 1], list_to_sort[i]
                swapped = True

        if not swapped:
            break

        swapped = False
        end_index -= 1

        for i in range(end_index - 1, start_index - 1, -1):
            if list_to_sort[i] > list_to_sort[i + 1]:
                list_to_sort[i], list_to_sort[i + 1] = list_to_sort[i + 1], list_to_sort[i]
                swapped = True

        start_index += 1

    return list_to_sort


input_list = [1, 2, 5, 8, 4, 5, 0, 3, 2]
print(bubble_sort_2_ways(input_list))
