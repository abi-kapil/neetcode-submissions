class Solution:

    def encode(self, strs: List[str]) -> str:
        response = ""
        for i in range(len(strs)):
            count = len(strs[i])
            response =  response + str(count) + "#"  + strs[i]
        return response

    def decode(self, s: str) -> List[str]:
        sample = s
        response = list()
        i = 0
        while i < len(s):
            j = i
            while s[j] != '#':
                j+=1
            count = int(s[i:j])
            response.append(s[j+1:j + 1 + count])
            i = j + 1 + count
        
        return response