class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        first = 0
        response = list()

        while first < len(nums):
            for second in range (first + 1, len(nums)):
                test = nums[first] + nums[second]
                if test == target:
                    response.append(first)
                    response.append(second)
                    first = len(nums) - 1
            first += 1

        return response