class Solution:
    def SmallerThanCurrentNumber(self, nums: List[int] -> List[int]):

        #Creating the Empty List 
        result = []

        # Iterating through the each nums
        for i in range(len(nums)):

            # Tracing it with Zero 0 - n-1
            count = 0 

            # In this we need to compare the both the elements i and j
            for j in range(len(nums)):

                # Check if its Smaller than this 
                if nums[j] < nums[i]:

                    # If it smaller we need to Count them in 
                    count +=1
                
                # And Apped then in the result (Count)
                result.append(count)
            
        # Return Result
        return result