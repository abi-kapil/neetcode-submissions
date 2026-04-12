class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        """
        run strs loop with each str
        run 26 char array, put char in the new array if its in the str
        check if the new array is a key in store and add 2, append these
        store array as key and value as 1
        """
        store = dict()

        for str in strs:

            arrChar = [0] * 26

            for c in str:
                arrChar[ord(c) - ord('a')] += 1

            my_arrChar = tuple(arrChar)
            print(my_arrChar)
            if my_arrChar in store:
                store[my_arrChar].append(str)
            else:
                store[my_arrChar] = [str]
        
        result = list()
        for value in store.values():
            result.append(value)

        return result

