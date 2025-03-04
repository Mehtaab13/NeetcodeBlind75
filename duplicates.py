def hasDuplicate(nums):
    my_dict = {}
    for num in nums:
        if num not in my_dict.keys():
            my_dict[num] = 1
        else:
            return True
    return False