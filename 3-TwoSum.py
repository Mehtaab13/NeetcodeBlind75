def twoSum(nums, target):
    my_dict = {}
    for i, n in enumerate(nums):
        difference = target - n
        if difference in my_dict and my_dict[difference] != i:
            return [my_dict[difference], i]
        my_dict[n] = i