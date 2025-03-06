class Solution:
        def twoSum(self, nums: List[int], target: int) -> List[int]:
                
                # In this We are Using HashMap Value : index
                hashmap = {}

                # for Loop eneumerate the Array it give both (i[n])
                for i , n in enumerate(nums):
                        
                        # Difference the Target 4 - 0 to (n-1) Store into Diff
                        diff = target - n

                        # IF we find the diff we need to return Value & Index
                        if diff in hashmap:
                                
                                # hashmp[diff]
                                return [hashmap[diff], i]
                        
                        hashmap[n] = i
                return