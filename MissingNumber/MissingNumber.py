class Solution:
    def MissingNumber (self, nums: List[int]) -> int:
        nums.sort()
        for indices in range(len(nums)):
            if indices != nums[indices]:
                return indices
        return len(indices)