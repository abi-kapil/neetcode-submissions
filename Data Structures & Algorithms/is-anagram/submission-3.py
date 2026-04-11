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
            if x not in store:
                return False
            else:
                store[x] -= 1
            if store[x] < 0:
                    return False
        
        return True
