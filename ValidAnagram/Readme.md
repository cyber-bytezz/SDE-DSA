📌 **Problem Statement:**  
Given two strings `s` and `t`, return `True` if `t` is an **anagram** of `s`, and `False` otherwise.

✅ **Anagram Definition:**  
An anagram is a word or phrase **formed by rearranging the letters** of another.  
💡 **Example:** `"listen"` → `"silent"`, `"anagram"` → `"nagaram"`

---
## **🚀 Thought Process Before Coding**
👉 If `s` and `t` have **different lengths**, they cannot be an anagram.  
👉 We need to **compare the frequency of characters** in both strings.  
👉 If both strings have **the same character counts**, they are an anagram.  
👉 The best way to store character counts is using a **dictionary (`{}` in Python)**.

---
## **📌 Step-by-Step Plan**
1. **Check if the lengths of `s` and `t` are different.**  
   - If yes → return `False` immediately.
2. **Create two dictionaries** to store character frequencies for `s` and `t`.
3. **Loop through both strings** and **count each character**.
4. **Compare both dictionaries.**  
   - If they are equal, return `True`.  
   - Else, return `False`.

---
## **🔥 Code Implementation (Hash Map Approach)**
```python
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # Step 1: If lengths are different, return False
        if len(s) != len(t):
            return False
        
        # Step 2: Create dictionaries to count character frequencies
        countS, countT = {}, {}

        # Step 3: Count character frequencies in both strings
        for i in range(len(s)):
            countS[s[i]] = 1 + countS.get(s[i], 0)
            countT[t[i]] = 1 + countT.get(t[i], 0)
        
        # Step 4: Compare both dictionaries
        return countS == countT
```
---
## **🔎 Explanation of Each Line**
### **1️⃣ Check Length First**
```python
if len(s) != len(t):
    return False
```
💡 **Why?**  
If two words have different lengths, they **cannot** be anagrams.  
✅ **Example:** `"abc"` vs. `"abcd"` → Return `False` because lengths differ.

---
### **2️⃣ Create Dictionaries for Character Counts**
```python
countS, countT = {}, {}
```
💡 **Why?**  
- `countS` stores **how many times each character appears in `s`**.  
- `countT` stores **how many times each character appears in `t`**.

---
### **3️⃣ Loop Through Both Strings**
```python
for i in range(len(s)):  
    countS[s[i]] = 1 + countS.get(s[i], 0)  
    countT[t[i]] = 1 + countT.get(t[i], 0)  
```
💡 **What happens here?**  
- `s[i]` picks each letter from `s`.  
- `t[i]` picks each letter from `t`.  
- **`.get(key, 0)`** ensures missing characters start from **0**.

✅ **Example Execution for `s = "banana"`**
| `i` | `s[i]` | `countS.get(s[i], 0)` | Update `countS` |
|----|------|----------------|----------------|
| 0  | `'b'`  | `0` → `1`  | `{'b': 1}` |
| 1  | `'a'`  | `0` → `1`  | `{'b': 1, 'a': 1}` |
| 2  | `'n'`  | `0` → `1`  | `{'b': 1, 'a': 1, 'n': 1}` |
| 3  | `'a'`  | `1` → `2`  | `{'b': 1, 'a': 2, 'n': 1}` |
| 4  | `'n'`  | `1` → `2`  | `{'b': 1, 'a': 2, 'n': 2}` |
| 5  | `'a'`  | `2` → `3`  | `{'b': 1, 'a': 3, 'n': 2}` |

---
### **4️⃣ Compare the Two Dictionaries**
```python
return countS == countT
```
💡 **Why?**  
- If both dictionaries store the **same character counts**, then `t` is an anagram of `s`.  
- Otherwise, `t` is **not an anagram**.

✅ **Example**
```python
s = "anagram"
t = "nagaram"
```
✔ Both count dictionaries are:  
```python
{'a': 3, 'n': 1, 'g': 1, 'r': 1, 'm': 1}
```
✔ **They match, so return `True`**.

---
## **📊 Time & Space Complexity Analysis**
| Approach | Time Complexity | Space Complexity |
|----------|---------------|----------------|
| **Hash Map Counting (Best)** | O(n) | O(1) |
| **Sorting Approach** | O(n log n) | O(1) |
| **Using `Counter` (Pythonic)** | O(n) | O(1) |

✅ **Best Approach:** **Hash Map (`O(n)`)**  
⚡ **Avoid Sorting (`O(n log n)`) as it's slower.**

---
## **🔥 Alternative Approaches**
### **1️⃣ Sorting Approach**
```python
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return sorted(s) == sorted(t)
```
✔ **Time Complexity:** `O(n log n)`  
❌ **Slower because sorting is expensive**.

---
### **2️⃣ Using `collections.Counter` (Most Pythonic)**
```python
from collections import Counter

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return Counter(s) == Counter(t)
```
✔ **Time Complexity:** `O(n)`  
✔ **Space Complexity:** `O(1)`  
✔ **Shorter, cleaner, and efficient.**  

---
## **🚀 Key Takeaways**
✅ **Step 1:** Check length first → if different, return `False`.  
✅ **Step 2:** Use **dictionaries (`{}`)** to store character counts.  
✅ **Step 3:** Loop through both strings → **increment character counts**.  
✅ **Step 4:** Compare both dictionaries → if equal, return `True`.  

---
## **💡 Frequently Asked Questions (FAQ)**
### **1️⃣ Why Use `.get(s[i], 0)`?**
- It avoids errors **if the key doesn’t exist**.
- If `s[i]` is not in `countS`, `.get()` returns `0`.

---
### **2️⃣ Why Compare `countS == countT`?**
- If two dictionaries store the **same character frequencies**, the words are anagrams.

---
### **3️⃣ When to Use Sorting Approach?**
- Only when **modifying input is allowed**.
- Sorting is **slower (`O(n log n)`)** than Hash Map (`O(n)`).

---
## **🎯 Final Advice**
✔ **Memorize this `O(n)` dictionary approach** → Best for interviews.  
✔ **Use `Counter(s) == Counter(t)`** for Pythonic readability.  
✔ **Avoid sorting unless required (`O(n log n)`).**  
