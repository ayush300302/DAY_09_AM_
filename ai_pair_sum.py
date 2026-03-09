# ai_pair_sum.py
# Day 9 AM - Lists Deep Dive
# Part D: AI-Augmented Task - Pair Sum


# -----------------------------------------------
# Step 1: Prompt used
# -----------------------------------------------
# "Write a Python function that finds all pairs in a list
#  that sum to a target number using list comprehensions."


# -----------------------------------------------
# Step 2: AI Generated Code (pasted as-is)
# -----------------------------------------------

def find_pairs_ai(lst, target):
    return [(lst[i], lst[j]) for i in range(len(lst))
            for j in range(i + 1, len(lst))
            if lst[i] + lst[j] == target]


# -----------------------------------------------
# Step 3: Testing AI code
# -----------------------------------------------

print("=== AI Code Tests ===")
print(find_pairs_ai([1, 2, 3, 4, 5], 6))   # [(1,5), (2,4)]
print(find_pairs_ai([1, 1, 1], 2))           # [(1,1), (1,1), (1,1)] <- duplicate pairs!


# -----------------------------------------------
# Issues found in AI code:
# 1. Duplicate pairs when list has repeated values
#    e.g. [1,1,1] gives 3 pairs of (1,1) — might not be desired
# 2. No deduplication of value-pairs
# 3. O(n^2) — not efficient for large lists
# -----------------------------------------------


# -----------------------------------------------
# Improved Version
# -----------------------------------------------

def find_pairs_improved(lst, target):
    """
    Returns unique value-pairs that sum to target.
    Avoids duplicate pairs like (1,1) appearing 3 times for [1,1,1].
    Uses a set to track seen pairs.
    """
    seen_pairs = set()
    result = []

    for i in range(len(lst)):
        for j in range(i + 1, len(lst)):
            if lst[i] + lst[j] == target:
                pair = tuple(sorted((lst[i], lst[j])))
                if pair not in seen_pairs:
                    seen_pairs.add(pair)
                    result.append(pair)
    return result


# O(n) solution using a set (finds first occurrence pairs, no duplicates by value)
def find_pairs_on(lst, target):
    """
    O(n) approach using a set.
    Finds pairs where a + b = target.
    Each unique value-pair is returned only once.
    """
    seen = set()
    result_pairs = set()

    for num in lst:
        complement = target - num
        if complement in seen:
            pair = tuple(sorted((num, complement)))
            result_pairs.add(pair)
        seen.add(num)

    return list(result_pairs)


print("\n=== Improved Version Tests ===")
print(find_pairs_improved([1, 2, 3, 4, 5], 6))  # [(1,5), (2,4)]
print(find_pairs_improved([1, 1, 1], 2))          # [(1,1)] - only once now

print("\n=== O(n) Set-based Version ===")
print(find_pairs_on([1, 2, 3, 4, 5], 6))         # {(1,5), (2,4)}
print(find_pairs_on([1, 1, 1], 2))                # {(1,1)}
