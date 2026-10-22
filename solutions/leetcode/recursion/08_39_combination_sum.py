class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:  # type: ignore # noqa: F821
        result = []

        def backTrack(start:int, current:List[int], total:int): # type: ignore  # noqa: F821
            if total == target:
                result.append(current.copy()) # type: ignore
                return 
            if total>target:
                return
            for i in range(start, len(candidates)): # type: ignore
                current.append(candidates[i]) # type: ignore
                backTrack(i, current, total + candidates[i]) # type: ignore
                current.pop() # type: ignore
        
        backTrack(0, [], 0) # type: ignore
        return result # type: ignore
