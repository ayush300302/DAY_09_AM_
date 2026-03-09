# AI Pair Sum — Analysis and Improvements

## Step 1: Prompt Used

> "Write a Python function that finds all pairs in a list that sum to a target number using list comprehensions."

---

## Step 2: AI Generated Code

```python
def find_pairs_ai(lst, target):
    return [(lst[i], lst[j]) for i in range(len(lst))
            for j in range(i + 1, len(lst))
            if lst[i] + lst[j] == target]
```

---

## Step 3: Testing the AI Code

```
find_pairs_ai([1, 2, 3, 4, 5], target=6)  →  [(1, 5), (2, 4)]   ✅ correct
find_pairs_ai([1, 1, 1], target=2)         →  [(1,1), (1,1), (1,1)]  ❌ duplicates!
```

---

## Issues Found

**1. Duplicate pairs with repeated values**
When the list has multiple identical values, the AI code returns the same value-pair multiple times. For `[1,1,1]` with target=2, we get `(1,1)` three times instead of once.

**2. O(n²) time complexity**
The nested loop approach checks every possible pair. For large lists this becomes slow. An O(n) solution is possible using a set.

---

## Improved Version

```python
def find_pairs_improved(lst, target):
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
```

**Improvement:** Uses a set to track already-found pairs so duplicates are skipped.

---

## O(n) Solution Using Sets

```python
def find_pairs_on(lst, target):
    seen = set()
    result_pairs = set()
    for num in lst:
        complement = target - num
        if complement in seen:
            pair = tuple(sorted((num, complement)))
            result_pairs.add(pair)
        seen.add(num)
    return list(result_pairs)
```

**Why O(n)?**  
Instead of checking every pair, we go through the list once. For each number, we calculate what value would complete the pair (`target - num`) and check if we've already seen it. Set lookups are O(1), so the whole function is O(n).

**Trade-off:** This approach only finds unique value-pairs, not index-pairs. If the problem needs index-level pairs, the O(n²) approach is still needed.

---

## Summary of Improvements

| Issue | AI Code | Improved Code |
|-------|---------|----------------|
| Duplicate pairs | Returns all | Deduplicates using set |
| Time complexity | O(n²) | O(n) using set trick |
| Handles [1,1,1], target=2 | 3 pairs | 1 pair |
