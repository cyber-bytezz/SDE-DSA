# **📌 Approach Used:**
This problem follows the **Two-Pointer Approach** and **String Manipulation**.

### **🔹 Encoding Approach**
- We traverse each word in the list.
- We store each word with its **length** and a **separator (`#`)**.
- The final encoded string looks like:  
  ```plaintext
  "5#apple6#banana6#cherry"
  ```
- This ensures **no data loss** when decoding.

### **🔹 Decoding Approach**
- We use **two pointers (`i` and `j`)** to process the encoded string.
- `i` starts at `0`, and `j` moves forward **until it finds `#`**.
- The number before `#` tells us **the length of the word**.
- We **extract the word**, store it, and move `i` forward to the next word.
- The process **repeats until we reach the end of the string**.

---

# **🖼️ Diagrams for Easy Understanding** 🎨

## **1️⃣ Encoding Process**  
**Input:** `["apple", "banana", "cherry"]`  
**Steps:**
```
Step 1: Take "apple" → Length = 5 → Store as "5#apple"
Step 2: Take "banana" → Length = 6 → Store as "6#banana"
Step 3: Take "cherry" → Length = 6 → Store as "6#cherry"
Final Encoded String: "5#apple6#banana6#cherry"
```

### **Visualization**
```
---------------------------------
|  5  |  #  | apple  | 
---------------------------------
|  6  |  #  | banana |
---------------------------------
|  6  |  #  | cherry |
---------------------------------
```
✅ The encoded string is:  
```plaintext
"5#apple6#banana6#cherry"
```

---

## **2️⃣ Decoding Process**
**Input:** `"5#apple6#banana6#cherry"`
**Steps:**
1. Start from index `0` → Read `5` → Extract `"apple"`.
2. Move forward → Read `6` → Extract `"banana"`.
3. Move forward → Read `6` → Extract `"cherry"`.

### **Visualization**
```
Encoded String: "5#apple6#banana6#cherry"
                 ↑
                 i (Start)
                 
Step 1: Find # → Read "5" → Extract "apple"
                 --------------
                 | 5#apple  |  
                 --------------

Move `i` forward to next number

Step 2: Find # → Read "6" → Extract "banana"
                 -------------------
                 | 6#banana  |  
                 -------------------

Move `i` forward to next number

Step 3: Find # → Read "6" → Extract "cherry"
                 -------------------
                 | 6#cherry  |  
                 -------------------

Final Decoded List: ["apple", "banana", "cherry"]
```
✅ The decoding correctly **reconstructs** the original words.

---

# **🚀 Approach Breakdown**
| Approach | Explanation |
|----------|------------|
| **Encoding** | Use **string concatenation** to store `length#word` for each word. |
| **Decoding** | Use a **Two-Pointer Approach**: `j` moves to find `#`, then extracts the word using its length. |
| **Efficiency** | Runs in **O(n) time complexity**, where `n` is the total length of all words. |

---

# **📝 Final Code (With Comments & Best Practices)**
```python
from typing import List

class Solution:
    def encode(self, words: List[str]) -> str:
        """
        Encodes a list of words into a single string.

        Approach:
        - Traverse each word in the list.
        - Store each word as `length#word`.
        - Ensures easy decoding later.

        Example:
        encode(["apple", "banana"]) → "5#apple6#banana"
        """
        encoded_string = ""
        for word in words:
            encoded_string += str(len(word)) + "#" + word  # Format: length#word
        return encoded_string

    def decode(self, encoded_string: str) -> List[str]:
        """
        Decodes a single string back into a list of words.

        Approach:
        - Use two pointers (`i` and `j`).
        - `j` finds `#` to determine the word's length.
        - Extract the word and move `i` forward.

        Example:
        decode("5#apple6#banana") → ["apple", "banana"]
        """
        decoded_words = []
        current_position = 0  # Pointer to track decoding position

        while current_position < len(encoded_string):
            separator_position = current_position  # Start looking for `#`

            while encoded_string[separator_position] != "#":
                separator_position += 1  # Move forward to find `#`

            word_length = int(encoded_string[current_position:separator_position])  # Extract length
            word_start = separator_position + 1  # Word starts after `#`
            word_end = word_start + word_length  # Calculate word end position
            
            decoded_words.append(encoded_string[word_start:word_end])  # Extract and store word
            current_position = word_end  # Move to next encoded word
        
        return decoded_words
```

---

# **🎯 Summary**
✅ **Encoding** → Converts a list of words into `"length#word"` format.  
✅ **Decoding** → Uses **two-pointer method** to extract words using `#`.  
✅ **Time Complexity** → **O(n)** (Processes each character once).  
✅ **Space Complexity** → **O(n)** (Stores the words in a list).  

---

# **💡 Next Steps**
Try encoding & decoding different lists:
```python
solution = Solution()
print(solution.encode(["hello", "world"]))  # Output: "5#hello5#world"
print(solution.decode("3#cat4#tree5#world"))  # Output: ["cat", "tree", "world"]
```
✅ **This will help reinforce your understanding!**  
