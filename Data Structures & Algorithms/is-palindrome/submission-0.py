class Solution:
    def isPalindrome(self, s: str) -> bool:
        front = 0
        clean_s = ''.join(c for c in s if c.isalnum()).lower()
        last = len(clean_s) - 1

        print(clean_s)
        while front <= last:
            print(f'front{front}')
            print(f'last{last}')
            if clean_s[front] != clean_s[last]:
                return False
            
            front += 1
            last -= 1
        
        return True
