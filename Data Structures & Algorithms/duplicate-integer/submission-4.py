class Solution(object):
    def hasDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        unique_numbers = set()
        for x in nums:
            if x in unique_numbers:
                return True
            else:
                unique_numbers.add(x)
        return False
