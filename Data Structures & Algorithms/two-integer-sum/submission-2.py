class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        store = {}
        idx = 0
        response = list()

        while idx < len(nums):
            key = nums[idx]
            left = target - key
            if left in store:
                response.append(nums.index(left))
                response.append(idx)
            else:
                store[key] = 0
        
            idx += 1

        return response