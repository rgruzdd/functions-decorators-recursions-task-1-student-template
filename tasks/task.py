from typing import List, Tuple, Union


def seq_sum(sequence: Union[List, Tuple]) -> int:
    """
    Add your code here or call it from here   
    """
    sum_numbers = 0
    for i in sequence:
        try:
            sum_numbers +=i
        except TypeError:
            sum_numbers += seq_sum(i)
    return sum_numbers

sequence = [1, 2, 3, [4, 5, (6, 7)]]

print(seq_sum(sequence))

