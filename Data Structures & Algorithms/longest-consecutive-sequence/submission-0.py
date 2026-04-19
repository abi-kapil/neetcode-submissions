class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        store = set()

        for i in nums:
                store.add(i)
        
        max = 0
        for num in store:
            if (num - 1) not in store:
                initial_val = num
                count = 1
                while (initial_val + 1) in store:
                    count += 1
                    initial_val += 1
                if max < count:
                    max = count
        
        return max
