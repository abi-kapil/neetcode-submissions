class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = nums[:]
        suffix = nums[:]
        print(prefix)
        print(suffix)

        for i in range (len(prefix)):
            if i != 0:
                prefix[i] = prefix[i-1] * nums[i-1]
            else: 
                prefix[i] = 1
        
        for i in range(len(suffix)-1,-1, -1):
            if i != len(suffix) - 1:
                suffix[i] = suffix[i+1] * nums[i+1]
            else:
                suffix[i] = 1
        print(prefix)
        print(suffix)

        for i in range(len(nums)):
            nums[i] = prefix[i] * suffix[i]
        
        return nums