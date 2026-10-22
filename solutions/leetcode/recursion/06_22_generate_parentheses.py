class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        result = []

        def backTrack(current:str, open_left:int, close_left:int):
            if open_left == 0 and close_left == 0:
                result.append(current)
                return 

            if open_left > 0:
                backTrack(current + '(', open_left-1, close_left)
            
            if open_left < close_left:
                backTrack(current + ')', open_left, close_left-1)
        
        backTrack("", n, n)
        return result
    
# Time Complexity O(nC_n)
# Space Complexity O(nC_n+n^2)=O(nC_n).