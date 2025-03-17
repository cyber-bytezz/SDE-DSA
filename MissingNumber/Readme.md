## ✅ **Problem Statement Recap**

You're given an array of unique numbers `nums` that contains numbers ranging from `0` to `n`, but one number in this range is missing. You need to find that missing number.

---

## 🚩 **Example**

```
Input: nums = [3,0,1]
Output: 2

Explanation:
Array has length n = 3.
Range of numbers should be [0, 1, 2, 3].
Numbers given: [0, 1, 3] (sorted), missing number is clearly 2.
```

---

## 🧑‍💻 **Your Python Solution Explained (Line by Line)**

### Code
```python
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nums.sort()
        for indi in range(len(nums)):
            if indi != nums[indi]:
                return indi
        return len(nums)
```

### Detailed Explanation

**Line 1**: 
```python
class Solution:
```
- Defines a class named `Solution`. LeetCode uses this class to run your solution.

---

**Line 2**:
```python
    def missingNumber(self, nums: List[int]) -> int:
```
- Defines a method (function within a class) called `missingNumber`.
- **self**: Standard first parameter for methods inside classes (it refers to the instance of the class, required syntax).
- **nums: List[int]**: Declares that `nums` is a list of integers.
- **-> int**: Indicates the function returns an integer (the missing number).

---

**Line 3**:
```python
        nums.sort()
```
- Sorts the array `nums` in ascending order.
- This makes it easy to find which number is missing because it organizes the numbers from smallest to largest.

**Example**:
- Before sorting: `[3,0,1]`
- After sorting: `[0,1,3]`

---

**Lines 4 and 5**:
```python
        for indi in range(len(nums)):
```
- Creates a loop that iterates over indices (`indi`) of the array `nums` from `0` up to `len(nums) - 1`.
- `range(len(nums))` generates numbers `[0, 1, 2, ..., len(nums) - 1]`.

---

**Lines 4-5**:
```python
            if indi != nums[indi]:
                return indi
```
- Checks if the current index (`indi`) matches the number at that index (`nums[indi]`).
- If they don't match, it means that the current number at that position is not the number we expect. This indicates that the current index itself is the missing number, so we return it immediately.

**Example**:
- Suppose `nums = [0, 1, 3]` after sorting:
  - `indi = 0`, `nums[0] = 0` (no issue)
  - `indi = 1`, `nums[1] = 1` (no issue)
  - `indi = 2`, `nums[2] = 3` **← mismatch detected**, so return `2`

---

**Line 6**:
```python
        return len(nums)
```
- This line executes only if the loop completes and no mismatch is found. It means all indices matched perfectly.
- The missing number is therefore the last number, which equals the length of `nums`.

**Example**:
- `nums = [0,1,2]` (after sorting, indices match perfectly)
- Missing number is `3` (since nums length is 3).

---

## 🚀 **Time and Space Complexity**

- **Time complexity**: `O(n log n)`
  - Sorting typically takes `O(n log n)` time.
- **Space complexity**: `O(1)` if ignoring sorting in-place.

---

## 🎯 **Optimized Follow-up Solution (Extra Info)**

You could achieve better (`O(n)` time, `O(1)` space) without sorting using arithmetic sum:

```python
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        expected_sum = n * (n + 1) // 2  # Sum of 0 to n
        actual_sum = sum(nums)           # Sum of given nums
        return expected_sum - actual_sum
```

- This solution calculates the sum of numbers from `0` to `n` and subtracts the sum of given numbers.
- Result is the missing number.

---

## 📌 **Key Concepts Learned**

- **Sorting:** Good for simple checks.
- **Index matching**: Comparing index vs. value to find missing number.
- **Edge case**: If no number missing from 0 to `len(nums)-1`, the missing number is `len(nums)`.
