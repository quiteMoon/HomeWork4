# Task 1
# def multiple(*numbers):    
#     n = 1
#     for i in numbers:
#         n *=i
#     return n

# print(multiple(1, 2, 3, 4, 5, 6))

# Task 2

# def minimum(*list):
#     minimum = min(list)
#     return minimum

# print(minimum(1, 2, 3, 4, 5, 6, 0))

# Task 3
# def count_primes_in_list(lst):
#     count = 0
#     for number in lst:
#         if number > 0:
#             count += 1
#     return count

# numbers_list = [2, 3, 5, 7, 11, 4, 8, 9, 13, -1, -4, -7, -54, -24]
# result = count_primes_in_list(numbers_list)
# print(f"Кількість простих чисел у списку: {result}")

# Task 4

# def delete_number(list, number):
#    count = 0
#    for i in list:
#        if i == number:
#            list.remove(i)
#            count += 1
#    return count

# numbers_list = [2, 3, 5, 2, 11, 4, 8, 2, 13, -1, -4, -7, -54, -24, 2]
# print(f"Кількість видалених елементів: {delete_number(numbers_list, 2)}")

# Task 5

# def combine_lists(*list1, list2):
#     comb = list1 + list2
#     return comb

# list1 = [10, 2, 34, 3, 39, 56, 7, 13]
# list2 = [4, 51, 6, 7, 8, 9, 41]

# combined_list = combine_lists(list1, list2)
# print(combined_list)

# Task 6

# def power(*lst, powerLevel):
#     result = []
#     for x in lst:
#         result.append(x**powerLevel)
#     return result

# nums = [1, 2, 3, 4, 5, 6, 7]
# powered = power(nums, 4)
# print(powered)