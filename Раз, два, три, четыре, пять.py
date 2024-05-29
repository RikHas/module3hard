data_structure = [[1, 2, 3], {'a': 4, 'b': 5}, (6, {'cube': 7, 'drum': 8}),
                  "Hello", ((), [{(2, 'Urban', ('Urban2', 35))}])]

def sum_numbers(data):
    total_sum = 0
    for i in data:
        if isinstance(i, int):
            total_sum += i
        elif isinstance(i, (list, tuple, set)):
            total_sum += sum_numbers(i)
        elif isinstance(i, dict):
            total_sum += sum_numbers(i.values())
    return total_sum
result = sum_numbers(data_structure)

def sum_string(data_structure):
    def sum_lengths(i):
        if isinstance(i, tuple):
            return sum(sum_lengths(sub_item) for sub_item in i)
        elif isinstance(i, str):
            return len(i)
        elif isinstance(i, (list, dict, set)):
            return sum(sum_lengths(sub_item) for sub_item in i)
        else:
            return 0

    return sum_lengths(data_structure)
result_2 = sum_string(data_structure)

print(result + result_2)
