## **🔹 Problem Explanation (Step 1 - What is the Goal?)**
You have a list of numbers (`nums`) and a target sum (`target`).  

👉 You need to find **two numbers** in `nums` that **add up to** `target`.  
👉 You **return the indices** of those two numbers.

✅ **Example**
```python
nums = [2, 7, 11, 15]
target = 9
```
✔ **Answer:** `[0, 1]`  
👉 Because **`nums[0] + nums[1] = 2 + 7 = 9`**

---

## **🔹 Now Let's Understand the Code (Step 2)**
```python
class Solution:
```
- `class` → A **blueprint** that holds functions.  
- `Solution` → The class name. (LeetCode requires this format).  

---

```python
    def twoSum(self, nums: List[int], target: int) -> List[int]:
```
- `def` → **Defines a function** (a reusable block of code).  
- `twoSum` → The **name of the function** (LeetCode calls it this).  
- `self` → **Refers to the object** of the class.  
- `nums: List[int]` → **Takes a list of numbers as input**.  
- `target: int` → **Takes an integer (`target`) as input**.  
- `-> List[int]` → **Says that this function returns a list of two numbers**.  

---

### **🔹 Creating an Empty Dictionary**
```python
        prevMap = {}  # val : index
```
- `prevMap = {}` → This **creates an empty dictionary**.  
- **Dictionary Explanation:**  
  - **Key:** The number in `nums`.  
  - **Value:** The index of that number in `nums`.  

✅ **Example Dictionary Usage**  
```python
prevMap = {2: 0}  # "2" is at index 0
```
If `prevMap = {2: 0, 7: 1}`, it means:
- **2 is stored at index `0`**  
- **7 is stored at index `1`**

---

### **🔹 Looping Through the Array**
```python
        for i, n in enumerate(nums):
```
- `for` → **Start a loop** (repeat steps for each number).  
- `enumerate(nums)` → **Gets both the index (`i`) and the number (`n`)**.  

✅ **Example of `enumerate(nums)`**
```python
nums = [2, 7, 11, 15]
# enumerate(nums) produces:
(0, 2)  # i = 0, n = 2
(1, 7)  # i = 1, n = 7
(2, 11) # i = 2, n = 11
(3, 15) # i = 3, n = 15
```
Each time, `i` is **the index** and `n` is **the number**.

---

### **🔹 Finding the Difference (`diff`)**
```python
            diff = target - n
```
- `target - n` → **What number do we need to reach `target`?**
- `diff` is that **missing number**.

✅ **Example Calculation**
```python
target = 9
n = 2  # First number in nums
diff = 9 - 2  # We need 7 to complete the sum
```
Now, we are looking for `7`.

---

### **🔹 Checking If We Already Saw That Number**
```python
            if diff in prevMap:
```
- `if diff in prevMap:` → **Check if `diff` exists in our dictionary.**  
- **If `diff` exists**, it means **we already saw the needed number before**.

✅ **Example Check**
```python
prevMap = {2: 0}  # We already saw "2" at index 0
diff = 7  # We are checking for "7"
```
- If `7` is in `prevMap`, then we **found our answer**.

---

### **🔹 Returning the Answer**
```python
                return [prevMap[diff], i]
```
- `prevMap[diff]` → **Gets the index of `diff` (the number we saw earlier).**  
- `i` → **Current index of `n` (the new number we are processing).**  
- **Returns the two indices as a list**.

✅ **Example Execution**
```python
prevMap = {2: 0}  # We already stored "2" at index 0
i = 1
diff = 7
# Since "7" was found, return:
return [0, 1]  # Index of "2" and "7"
```

---

### **🔹 Storing the Number in `prevMap`**
```python
            prevMap[n] = i
```
- **We store the current number (`n`) and its index (`i`).**  
- This helps us find the answer faster in future iterations.

✅ **Example Updates:**
1. `nums[0] = 2` → `prevMap = {2: 0}`
2. `nums[1] = 7` → `prevMap = {2: 0, 7: 1}`
3. `nums[2] = 11` → `prevMap = {2: 0, 7: 1, 11: 2}`

---

### **🔹 If No Answer is Found**
```python
        return
```
- If **no answer is found**, the function **returns nothing (`None`)**.  
- **But this should never happen**, because the problem guarantees a solution.

---

## **🚀 Full Execution Example**
### **Input:**
```python
nums = [2, 7, 11, 15]
target = 9
```
### **Step-by-Step Execution**
| Step | `i` | `n` | `diff = target - n` | `prevMap` | Action |
|------|----|----|------------------|---------|---------|
| 1️⃣ | 0  | 2  | `9 - 2 = 7` | `{}` | Store `{2: 0}` |
| 2️⃣ | 1  | 7  | `9 - 7 = 2` | `{2: 0}` | `2` exists! Return `[0, 1]` |

✔ **Final Output:** `[0, 1]`

---

## **📊 Time and Space Complexity Analysis**
| Complexity | Explanation |
|------------|-------------|
| **Time Complexity**: `O(n)` | We loop through `nums` once (`O(n)`). Dictionary operations (`in` & `get`) are `O(1)`. |
| **Space Complexity**: `O(n)` | We store at most `n` elements in `prevMap` (worst case). |

---

## **🔥 Alternative Approach (Brute Force)**
```python
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]
```
🔹 **Time Complexity:** `O(n^2)` (Slow)  
🔹 **Space Complexity:** `O(1)` (No extra storage)  

⚡ **Why is Hash Map (`O(n)`) Better?**  
- This avoids checking every pair (`O(n^2)`).
- Uses dictionary lookups (`O(1)`) for **fast access**.

---

## **🎯 Final Takeaways**
✔ **Step 1:** Use a **dictionary** to store numbers we've seen.  
✔ **Step 2:** For each number, compute `diff = target - n`.  
✔ **Step 3:** If `diff` exists in `prevMap`, return `[prevMap[diff], i]`.  
✔ **Step 4:** If not, store the current number in `prevMap` for future reference.  
✔ **Final Complexity:** `O(n)` **(efficient solution)** ✅  
