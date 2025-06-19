# 1 sum nested list

def sum_nested(lst):
    total = 0
    for item in lst:
        if isinstance(item, (int,float)):
            total += item
        else:
            total += sum_nested(item)
    return total

print(sum_nested([1, [2, 3], [4, [5]]])) # 15

"""
Base Case: Adds numbers directly.

Recursive Case: Recursively sums nested lists.

Iterates through elements; numbers are summed, lists trigger recursive calls. Handles arbitrary nesting levels.
"""