def choose_func(nums: list[int], func_1, func_2):
    var = all(num >= 0 for num in nums)
    if var:
        return square_nums(nums=nums)
    else:
        return remove_negatives(nums=nums)


def square_nums(nums):
    return [num ** 2 for num in nums]


def remove_negatives(nums):
    return [num for num in nums if num > 0]


def main():
    nums1 = [1, 2, 3, 4, 5]
    nums2 = [1, -2, 3, -4, 5]

    assert choose_func(nums1, square_nums, remove_negatives) == [1, 4, 9, 16, 25]
    assert choose_func(nums2, square_nums, remove_negatives) == [1, 3, 5]


if __name__ == '__main__':
    main()
