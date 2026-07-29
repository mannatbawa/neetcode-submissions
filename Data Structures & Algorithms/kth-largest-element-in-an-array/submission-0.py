import random 
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        pivot = random.choice(nums)
        
        greater = []
        smaller = []
        equal = []

        for num in nums:
            if num < pivot:
                smaller.append(num)
            elif num > pivot:
                greater.append(num)
            else:
                equal.append(num)
        
        #pivot is in greater array
        if k <= len(greater):
            return self.findKthLargest(greater, k)
        elif k > len(greater) + len(equal):
            new_k = k - len(greater) - len(equal)
            return self.findKthLargest(smaller, new_k)       
        else:
            return pivot

            

