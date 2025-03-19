## **Full Code:**
```python
from typing import List

class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        result = []
        
        for i in range(len(nums)):  # Iterate through each number
            count = 0
            for j in range(len(nums)):  # Compare with all other numbers
                if nums[j] < nums[i]:  # Count numbers smaller than nums[i]
                    count += 1
            result.append(count)  # Store the count for nums[i]
        
        return result
```

---

## **Line-by-Line Explanation**

### **1️⃣ Importing the `List` Type (Optional)**
```python
from typing import List
```
- `from typing import List` → This **imports** `List` from Python’s `typing` module.
- It is **optional** but used to define the input type for better readability.

---

### **2️⃣ Defining the Solution Class**
```python
class Solution:
```
- `class Solution:` → Creates a **class named `Solution`**.
- A **class** is a way to group related functions together.

---

### **3️⃣ Defining the Function (`smallerNumbersThanCurrent`)**
```python
def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
```
- `def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:`
  - `def` → **Defines a function** (a block of reusable code).
  - `smallerNumbersThanCurrent` → The **name** of our function.
  - `self` → Used because the function is inside a **class**.
  - `nums: List[int]` → The function takes **one parameter**, `nums`, which is a **list of integers**.
  - `-> List[int]` → Means the function **returns a list of integers**.

📌 **Example Input:**
```python
nums = [8, 1, 2, 2, 3]
```

---

### **4️⃣ Initializing the Result List**
```python
result = []
```
- Creates an **empty list** called `result` where we will store the output.
- This list will **store how many numbers are smaller than each number** in `nums`.

📌 **After this line:**
```python
result = []
```

---

### **5️⃣ First Loop – Iterating Over Each Number in `nums`**
```python
for i in range(len(nums)):  # Iterate through each number
```
- `for i in range(len(nums)):` → Loops **through each number in the list**.
- `range(len(nums))` → Generates a sequence of indices from `0` to `len(nums) - 1`.

📌 **Example for `nums = [8, 1, 2, 2, 3]`:**
```python
i = 0 → nums[0] = 8
i = 1 → nums[1] = 1
i = 2 → nums[2] = 2
i = 3 → nums[3] = 2
i = 4 → nums[4] = 3
```

---

### **6️⃣ Initializing `count` to Zero**
```python
count = 0
```
- `count = 0` → Starts a counter to track **how many numbers are smaller than `nums[i]`**.

📌 **For `nums[0] = 8`**
```python
count = 0
```

---

### **7️⃣ Second Loop – Comparing `nums[i]` with All Other Numbers**
```python
for j in range(len(nums)):  # Compare with all other numbers
```
- This is another loop inside the **first loop**.
- `for j in range(len(nums)):` → Loops through **all numbers again**.
- **Purpose**: To compare `nums[i]` with every `nums[j]`.

📌 **At `i = 0` (Checking `nums[0] = 8`):**
- `j = 0`, `nums[0] = 8` (Same number, skip)
- `j = 1`, `nums[1] = 1` (1 is smaller → `count += 1`)
- `j = 2`, `nums[2] = 2` (2 is smaller → `count += 1`)
- `j = 3`, `nums[3] = 2` (2 is smaller → `count += 1`)
- `j = 4`, `nums[4] = 3` (3 is smaller → `count += 1`)

📌 **Final `count = 4` for `nums[0] = 8`**.

---

### **8️⃣ Checking if `nums[j] < nums[i]`**
```python
if nums[j] < nums[i]:  # Count numbers smaller than nums[i]
```
- `nums[j] < nums[i]` → **Checks if `nums[j]` is smaller than `nums[i]`**.
- If true, increase `count`:
```python
count += 1
```

📌 **Example:**
```python
nums = [8, 1, 2, 2, 3]
For nums[0] = 8:
  nums[1] = 1  ✅ count += 1
  nums[2] = 2  ✅ count += 1
  nums[3] = 2  ✅ count += 1
  nums[4] = 3  ✅ count += 1
Final count = 4
```

---

### **9️⃣ Storing the Count in `result`**
```python
result.append(count)  # Store the count for nums[i]
```
- `result.append(count)` → Adds the count to the `result` list.
- This ensures each `nums[i]` gets its respective count.

📌 **Example for `nums = [8, 1, 2, 2, 3]`**
```python
result = [4, 0, 1, 1, 3]
```

---

### **🔟 Returning the Final Output**
```python
return result
```
- `return result` → **Returns the final list**.

📌 **Final Output for `nums = [8, 1, 2, 2, 3]`:**
```python
[4, 0, 1, 1, 3]
```

---

## **🔬 Complete Example Execution**
| `nums[i]` | Numbers Smaller than `nums[i]` | `count` |
|-----------|-------------------------------|--------|
| `8` | `[1, 2, 2, 3]` | `4` |
| `1` | `[]` (No smaller numbers) | `0` |
| `2` | `[1]` | `1` |
| `2` | `[1]` | `1` |
| `3` | `[1, 2, 2]` | `3` |

✅ **Final Output:**
```python
[4, 0, 1, 1, 3]
```

---

## **🛠 Time & Space Complexity**
| Step | Complexity |
|------|------------|
| Outer Loop (`for i`) | **O(n)** |
| Inner Loop (`for j`) | **O(n)** |
| **Total Complexity** | **O(n²)** (Very slow for large `n`) |

🚀 **This is the brute-force approach.**  
A faster solution uses sorting + a dictionary (`O(n log n)`).