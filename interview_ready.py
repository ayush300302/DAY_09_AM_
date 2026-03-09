# interview_ready.py
# Day 9 AM - Lists Deep Dive
# Part C: Conceptual + Coding + Debug

import copy

# -----------------------------------------------
# Q2: List Rotation
# -----------------------------------------------

def rotate_list(lst, k):
    if not lst:
        return lst
    k = k % len(lst)   # handles k > len(lst)
    # Rotate right by k: take last k elements and put them in front
    return lst[-k:] + lst[:-k]


# -----------------------------------------------
# Q3: Debug - modifying list while iterating
# -----------------------------------------------

# Buggy version (DO NOT USE):
# for num in nums:
#     if num % 2 == 0:
#         nums.remove(num)
# Bug: when we remove an element, the iterator skips the next element
# because the list shifts. For [2,4,6,8], result is [4,8] instead of []

# Fixed version:
def remove_evens(nums):
    return [num for num in nums if num % 2 != 0]


# -----------------------------------------------
# Test runs
# -----------------------------------------------

if __name__ == "__main__":
    # Q2 tests
    print("=== List Rotation ===")
    print(rotate_list([1, 2, 3, 4, 5], 2))   # [4, 5, 1, 2, 3]
    print(rotate_list([1, 2, 3, 4, 5], 7))   # same as k=2 (7%5=2)
    print(rotate_list([], 3))                  # []

    # Q3 tests
    print("\n=== Remove Evens (Fixed) ===")
    print(remove_evens([1, 2, 3, 4, 5, 6, 7, 8]))  # [1, 3, 5, 7]
    print(remove_evens([2, 4, 6, 8]))               # []

    # Q1 demo: shallow vs deep copy
    print("\n=== Shallow vs Deep Copy ===")
    original = [[1, 2], [3, 4]]

    shallow = copy.copy(original)
    deep = copy.deepcopy(original)

    original[0][0] = 99

    print("Original after change:", original)   # [[99, 2], [3, 4]]
    print("Shallow copy:", shallow)             # [[99, 2], [3, 4]] <- changed!
    print("Deep copy:", deep)                   # [[1, 2], [3, 4]]  <- unchanged
