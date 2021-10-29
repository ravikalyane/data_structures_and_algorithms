import datetime
import time
import random


def linear_search(my_list, target):
    start_time = datetime.datetime.now()
    count = 0
    for i in my_list:
        if i == target:
            end_time = datetime.datetime.now()
            linear_search_time = end_time - start_time
            return f'Linear Search: Completed in {count} iterations and index of target ({target}) is {count}. Time taken = {linear_search_time}'
        count += 1


def binary_search(my_list, target):
    start_time = datetime.datetime.now()
    left_index = 0
    right_index = len(my_list) - 1
    count = 0
    while left_index <= right_index:
        count += 1
        mid_index = (right_index + left_index) // 2
        if my_list[mid_index] == target:
            end_time = datetime.datetime.now()
            binary_search_time = end_time - start_time
            return f'Binary Search: Completed in {count} iterations and index of target ({target}) is {mid_index}. Time taken = {binary_search_time}'
        elif my_list[mid_index] < target:
            left_index = mid_index + 1
        else:
            right_index = mid_index - 1
    end_time = datetime.datetime.now()
    binary_search_time = end_time - start_time
    return 'Target not found.'


if __name__ == '__main__':
    my_list = []
    for i in range(10000):
        my_list.append(random.randint(1, 999999))
    my_list = list(sorted(set(my_list)))
    target = my_list[random.randint(1, 9999)]
    print("Target:", target)
    print(linear_search(my_list, target))
    print(binary_search(my_list, target))
