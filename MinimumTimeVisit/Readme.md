# **📌 Minimum Time Visiting All Points**
This repository contains a Python solution to the **LeetCode problem: Minimum Time Visiting All Points**. The goal is to find the shortest time required to visit all given points on a **2D grid** by moving **horizontally, vertically, or diagonally**.

---

## **📝 Problem Statement**
On a **2D plane**, you are given `n` points with integer coordinates:

```python
points = [[x1, y1], [x2, y2], ..., [xn, yn]]
```
You need to **visit these points in the given order** while following these movement rules:
1. Move **left or right** by 1 unit in 1 second.
2. Move **up or down** by 1 unit in 1 second.
3. Move **diagonally** (one unit both horizontally and vertically) in 1 second.

### **🎯 Objective**
Return the **minimum time (in seconds)** required to visit all the points in the order given.

---

## **📌 Example Walkthrough**
### **Example 1**
#### **Input**
```python
points = [[1,1], [3,4], [-1,0]]
```
#### **Step-by-Step Movement**
1. Move from **(1,1) → (3,4)**  
   - **Horizontal distance:** `|3 - 1| = 2`
   - **Vertical distance:** `|4 - 1| = 3`
   - **Time taken:** `max(2, 3) = 3` seconds.

2. Move from **(3,4) → (-1,0)**  
   - **Horizontal distance:** `|-1 - 3| = 4`
   - **Vertical distance:** `|0 - 4| = 4`
   - **Time taken:** `max(4, 4) = 4` seconds.

#### **Output**
```python
7
```
✅ **Total time to visit all points = 7 seconds**.

---

### **Example 2**
#### **Input**
```python
points = [[3,2], [-2,2]]
```
#### **Step-by-Step Movement**
1. Move from **(3,2) → (-2,2)**
   - **Horizontal distance:** `|-2 - 3| = 5`
   - **Vertical distance:** `|2 - 2| = 0` (stable y)
   - **Time taken:** `max(5, 0) = 5` seconds.

#### **Output**
```python
5
```
✅ **Total time to visit all points = 5 seconds**.

---

## **📌 Approach & Formula**
### **🔹 How Do We Calculate the Shortest Time?**
To move from **(x1, y1) → (x2, y2)**, we use the formula:

```python
time = max(abs(x2 - x1), abs(y2 - y1))
```
- `abs(x2 - x1)`: **Horizontal distance**.
- `abs(y2 - y1)`: **Vertical distance**.
- **Why `max()`?**  
  - If you move **diagonally**, both x and y decrease at the same time.
  - The **larger** of the two distances determines the minimum time required.

---

## **🖥️ Code Implementation**
```python
def minTimeToVisitAllPoints(points):
    total_time = 0  # Start with zero time

    for i in range(len(points) - 1):  # Loop through each pair of points
        x1, y1 = points[i]     # Get the current point
        x2, y2 = points[i + 1]  # Get the next point

        time = max(abs(x2 - x1), abs(y2 - y1))  # Use max() to calculate time

        total_time += time  # Add the calculated time to total_time

    return total_time  # Return the final total time
```

---

## **📌 Code Explanation (Line by Line)**
1. **Define Function**
   ```python
   def minTimeToVisitAllPoints(points):
   ```
   - Creates a function that takes `points` as input.

2. **Initialize Total Time**
   ```python
   total_time = 0
   ```
   - Starts at **0** since we haven't moved yet.

3. **Loop Through Each Pair of Points**
   ```python
   for i in range(len(points) - 1):
   ```
   - Moves from **each point to the next**.

4. **Extract Current and Next Points**
   ```python
   x1, y1 = points[i]
   x2, y2 = points[i + 1]
   ```
   - Stores `x` and `y` values for the **current** and **next** points.

5. **Calculate Movement Time**
   ```python
   time = max(abs(x2 - x1), abs(y2 - y1))
   ```
   - Uses **`max()` formula** to determine the shortest possible time.

6. **Update Total Time**
   ```python
   total_time += time
   ```
   - Adds `time` to `total_time`.

7. **Return Final Answer**
   ```python
   return total_time
   ```
   - **Returns** the total time to visit all points.

---

## **📌 Complexity Analysis**
| Factor | Explanation |
|--------|------------|
| **Time Complexity** | **O(n)** → We only loop through the points once. |
| **Space Complexity** | **O(1)** → We use only a single variable (`total_time`). |

---

## **🛠️ Running the Code**
To test the function, run:
```python
print(minTimeToVisitAllPoints([[1,1], [3,4], [-1,0]]))  # Output: 7
print(minTimeToVisitAllPoints([[3,2], [-2,2]]))  # Output: 5
```

---

## **📌 Key Takeaways**
✅ **Diagonal moves are preferred** (shortest path).  
✅ **Use the formula** `max(abs(x2 - x1), abs(y2 - y1))`.  
✅ **Loop through all points and add up the time**.  
✅ **Simple and efficient** with **O(n) time complexity**.  
