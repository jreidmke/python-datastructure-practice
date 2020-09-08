def mode(nums):
    """Return most-common number in list.

    For this function, there will always be a single-most-common value;
    you do not need to worry about handling cases where more than one item
    occurs the same number of times.

        >>> mode([1, 2, 1])
        1

        >>> mode([2, 2, 3, 3, 2])
        2
    """
    most_frequent = nums[0]
    count = nums.count(nums[0])
    for num in nums:
        if nums.count(num) > count:
            most_frequent = num
    return most_frequent

print(mode([1, 2, 1]))
print(mode([2, 2, 3, 3, 2]))