class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max = 0
        quantity = 0
        for i in range(len(heights)):
            
            for j in range(i + 1, len(heights)):
                
                if heights[i] < heights[j]:
                    quantity = heights[i] * (j - i)
                else:
                    quantity = heights[j] * (j - i)

                if quantity > max:
                    max = quantity
            
        
        return max