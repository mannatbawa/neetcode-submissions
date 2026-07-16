class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        map = {}
        for i, value in enumerate(nums):	
            complement = target - value
            if complement in map:
                return [map[complement], i]
            map[value] =  i
