def isAnagram(s, t):
    my_dict1 = {}
    my_dict2 = {}
    for letter in s:
        if letter not in my_dict1.keys():
            my_dict1[letter] = 1
        else:
            my_dict1[letter] = my_dict1[letter] + 1
    for letter in t:
        if letter not in my_dict2.keys():
            my_dict2[letter] = 1
        else:
            my_dict2[letter] = my_dict2[letter] + 1
    return my_dict1 == my_dict2