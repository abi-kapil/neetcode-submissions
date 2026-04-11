class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        store = {}

        if(len(s) != len(t)):
            return False

        for x in s:
            if x in store:
                store[x] += 1
            else:
                store[x] = 1
        
        for x in t:
            if x in store:
                store[x] -= 1
            else:
                return False
            if store[x] < 0:
                    return False
        
        return True
