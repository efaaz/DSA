class Solution:
    def letterCombinations(self, digits: str) -> list[str]:
        if not digits:
            return []
        phone_map = {
            '2':'abc', '3':'def', '4':'ghi', '5':'jkl', '6':'mno', '7':'pqrs', '8':'tuv', '9':'wxyz'
        }
        result = []
        def backTrack(index:int, current:int):
            if index == len(digits):
                result.append(current)
                return

            for char in phone_map[digits[index]]:
                backTrack(index+1, current + char) # type: ignore
        
        backTrack(0, "") # type: ignore
        return result
        