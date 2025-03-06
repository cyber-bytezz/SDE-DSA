class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        """
        Function to check if a list contains duplicate values.
        Returns True if there is a duplicate, otherwise False.
        """

        # Create an empty set to store unique numbers
        hashset = set()  # Set is used because lookup operations are O(1)

        # Iterate over each number in the list
        for n in nums:
            # If the number is already in the set, return True (duplicate found)
            if n in hashset:
                return True  # Exit function immediately since we found a duplicate
            
            #  Otherwise, add the number to the set (mark as seen)
            hashset.add(n)

        # If no duplicates are found, return False
        return False
