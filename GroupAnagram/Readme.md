## **Problem Statement**
Given a list of strings, we need to group words that are anagrams of each other. An anagram is a word formed by rearranging the letters of another word.

### **Example:**
#### **Input:**
```python
strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
```
#### **Output:**
```python
[["eat", "tea", "ate"], ["tan", "nat"], ["bat"]]
```

---

## **Full Code:**
```python
from collections import defaultdict
from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)  # Step 1: Create a dictionary to store anagrams

        for s in strs:  # Step 2: Loop through each word in the list
            count = [0] * 26  # Step 3: Create a list of 26 zeros for counting letters

            for c in s:  # Step 4: Loop through each letter in the word
                count[ord(c) - ord("a")] += 1  # Step 5: Increase the count for the letter

            res[tuple(count)].append(s)  # Step 6: Convert count to tuple & store in dictionary

        return res.values()  # Step 7: Return all grouped anagrams
```

---

## **Step-by-Step Explanation**

### **1️⃣ Import Required Libraries**
```python
from collections import defaultdict
from typing import List
```
✅ `defaultdict(list)`: Creates a dictionary where keys are automatically assigned an empty list if they don’t exist.
✅ `List`: Used for type hinting to indicate that `strs` is a list of strings, and the function returns a list of lists of strings.

---

### **2️⃣ Define the Function**
```python
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
```
✅ Defines a function inside a class.
✅ Takes `strs`, a **list of words** (e.g., `["eat", "tea", "tan", "ate", "nat", "bat"]`).
✅ Returns a **list of lists**, where each list contains **grouped anagrams**.

---

### **3️⃣ Create a Dictionary to Store Anagrams**
```python
res = defaultdict(list)
```
✅ Creates an **empty dictionary** where keys are **tuples representing letter frequencies**.
✅ **Automatically initializes an empty list** when a new key is added.

---

### **4️⃣ Loop Through Each Word in the List**
```python
for s in strs:
```
✅ Iterates through each word in the input list.
✅ **Example Iteration:**
1. `s = "eat"`
2. `s = "tea"`
3. `s = "tan"`
4. `s = "ate"`
5. `s = "nat"`
6. `s = "bat"`

---

### **5️⃣ Create a List of 26 Zeros for Letter Frequency**
```python
count = [0] * 26
```
✅ Creates a list of **26 zeros** (one for each lowercase letter `a-z`).
✅ Example before processing any word:
```python
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
```

---

### **6️⃣ Count Each Letter in the Word**
```python
for c in s:
    count[ord(c) - ord("a")] += 1
```
✅ **Find the index for each letter**:
- `ord("a") - ord("a") = 0` → stored at index `0`.
- `ord("b") - ord("a") = 1` → stored at index `1`.
- `ord("e") - ord("a") = 4` → stored at index `4`.

✅ **Example: Processing "eat"**
1. `"e"` → `count[4] += 1`
2. `"a"` → `count[0] += 1`
3. `"t"` → `count[19] += 1`

✅ **Final count list for "eat"**:
```python
[1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0]
```

---

### **7️⃣ Convert `count` List to a Tuple & Store in Dictionary**
```python
res[tuple(count)].append(s)
```
✅ Since lists **cannot be dictionary keys**, we convert `count` to a **tuple**.
✅ If the tuple **already exists**, we **append** the word to the existing list.
✅ If the tuple **does not exist**, it **creates a new list**.

---

### **8️⃣ Return the Grouped Anagrams**
```python
return res.values()
```
✅ `res.values()` returns all **grouped words** as a list of lists.
✅ **Final Output:**
```python
[["eat", "tea", "ate"], ["tan", "nat"], ["bat"]]
```

---

## **🔹 Why This Approach Works Efficiently?**
- **Letter frequency is used instead of sorting** → More efficient (`O(m * n)`).
- **Anagrams have the same tuple key** → Stored in the same list.
- **Fast lookup using a dictionary** (`defaultdict`).

---

## **🌟 Final Recap**
✅ **Step 1:** Create a dictionary to store anagram groups.
✅ **Step 2:** Iterate through each word.
✅ **Step 3:** Count letters using a list of size 26.
✅ **Step 4:** Convert the count list into a tuple.
✅ **Step 5:** Use the tuple as a key to store anagrams in the dictionary.
✅ **Step 6:** Return all grouped anagrams.
