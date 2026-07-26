class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix_sum = {}
        # map prefix_sum to number of time seen
        prefix_sum[0] = 1
        running_sum = 0
        num_arrays = 0
        for i, num in enumerate(nums):
            running_sum += num
            # right prefix - left prefix = k
            left_prefix = running_sum - k
            if left_prefix in prefix_sum:
                num_arrays += prefix_sum[left_prefix]
                
            if running_sum not in prefix_sum:
                prefix_sum[running_sum] = 1
            else:
                prefix_sum[running_sum]+=1

        
            
        return num_arrays

        