# 3 recursive search

def find_item(lst, target):
    for item in lst:
        if isinstance(item, list):
            if find_item(item, target):
                return True
        elif item == target:
            return True
    return False

print(find_item([1, [2, 3, [4]], 5], 4))  # Output: True