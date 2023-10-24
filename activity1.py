# unsorted_list = [
#     ("English", 88),
#     ("Science", 90),
#     ("Maths", 97),
#     ("Social sciences", 82),
# ]
# unsorted_list.sort(key=lambda x: x[1])
# print(unsorted_list)

# original_list = [3, 6, 9, 2]
# my_list = [i * i * i for i in original_list]
# print(my_list)

input_list = [3, 6, 9, 2]

even_or_odd = lambda num: num % 2 == 0

my_list = [even_or_odd(i) for i in input_list]
print(my_list)

list_comp = [i for i in range(101)]
print(list_comp)

input = "The quick brown fox jumped over the fence."
my_dict = {word: len(word) for word in input.split()}
print(my_dict)
