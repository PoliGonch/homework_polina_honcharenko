def binary_search_recursive(input_list, search_value, first=0, last=None):
    if last is None:
        last = len(input_list) - 1
    if first > last:
        raise ValueError

    mid = (first + last) // 2
    if input_list[mid] == search_value:
        return mid

    elif input_list[mid] > search_value:
        return binary_search_recursive(input_list, last=mid - 1, search_value=search_value)
    return binary_search_recursive(input_list, first=mid + 1, last=len(input_list) - 1, search_value=search_value)


print(binary_search_recursive([10, 20, 30, 40, 50, 60], 20))
