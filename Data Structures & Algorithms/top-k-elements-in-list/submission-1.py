class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        store = {}

        for i in nums:
            if i in store:
                store[i] += 1
            else:
                store[i] = 1

        sorted_store = dict(sorted(store.items(), key=lambda item: item[1], reverse=True))

        return list(sorted_store.keys())[:k]