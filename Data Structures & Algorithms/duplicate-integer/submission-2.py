class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        mySet = set();
        for each in nums:
            if each in mySet:
                return True
            else:
                mySet.add(each)
        return False