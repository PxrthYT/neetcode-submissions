class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        got_it = set()
        for num in nums:
            if num in got_it:
                return True
            got_it.add(num)
        return False
       
     
                