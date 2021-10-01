nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# # ***********************************
# my_list = []
# for n in nums:
#     my_list.append(n)

# # ***********************************
# my_list_comp = [n for n in nums]


# # ***********************************
# my_list_comp_sqrt = [n * n for n in nums]


# # ***********************************
# my_list_lambda = list(map(lambda n: (n * n), nums))


# # ***********************************
# my_list = []
# for n in nums:
#     if n % 2 == 0:
#         my_list.append(n)

# my_list = [n for n in nums if n % 2 == 0]

# my_list = list(filter(lambda n: n % 2 == 0, nums))


# # ***********************************
# my_list = []
# for letter in 'abcd':
#     for num in range(4):
#         my_list.append((letter, num))

# my_list = [(letter, num) for letter in 'abcd' for num in range(4)]

# names = ['Bruce', 'Clark', 'Peter', 'Logan', 'Wade']
# heros = ['Batman', 'Superman', 'Spiderman', 'Wolverine', 'Deadpool']

# print(list(zip(names, heros)))

# my_dict = {}
# for name, hero in zip(names, heros):
#     my_dict[name] = hero

# my_dict = {name: hero for name, hero in zip(names, heros) if name != 'Peter'}
# print(my_dict)

# nums = [1, 2, 2, 4, 4, 5, 7, 8, 9, 6, 5, 4, 1, 2, 3, 5, 4, 7, 8, 9, 6, 5, 4]
# my_set = set()
# print(my_set)
# for n in nums:
#     my_set.add(n)

# my_set = {n for n in nums}
# print(my_set)

def gen_func(nums):
    for n in nums:
        yield n * n


# my_gen = gen_func(nums)
my_gen = (n * n for n in nums)

for i in my_gen:
    print(i)
