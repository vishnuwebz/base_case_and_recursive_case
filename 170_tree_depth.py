# 4 tree depth

def max_depth(tree):
    if not isinstance(tree, list) or not tree:
        return 0
    return 1 + max(max_depth(child) for child in tree)

print(max_depth([1, [2, [3]], [4]])) # 3

"""
Base Case: Non-list or empty list returns 0.
Recursive Case: Adds 1 to max depth of children.
"""