from typing import List  # Import List for type hints

class Solution:
    def TopKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        # Create a Dictionary to Store Each Number's Frequency
        frequency_map = {}  # Dictionary to store frequency of numbers

        # Count occurrences of each number in nums
        for num in nums:

            # If num already exists in the dictionary, increase its count by 1
            # If num is not in the dictionary, start its count at 1
            frequency_map[num] = 1 + frequency_map.get(num, 0)

        # Create a "Bucket" list where index represents the frequency
        # Each index i will store numbers that appear i times
        bucket = [[] for _ in range(len(nums) + 1)]  # Creating empty buckets

        # Step 4: Place numbers into their respective frequency buckets
        for num, count in frequency_map.items():
            bucket[count].append(num)  # Store number in the correct frequency index

        # Step 5: Collect the Top K Frequent Numbers
        result = []  # This list will store the final top K frequent numbers

        # Start from the highest frequency (end of bucket) and move towards 1
        for i in range(len(bucket) - 1, 0, -1):
            for num in bucket[i]:  # Go through all numbers in this frequency bucket
                result.append(num)  # Add number to the result list
                
                # If we have collected K elements, return the result immediately
                if len(result) == k:
                    return result