class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hashmap = {}
        count = 1
        longest = 1
        sortedlist = sorted(nums)
        for i in range (len(sortedlist) - 1):
           
            if sortedlist[i] == sortedlist[i+1]:
                continue
            if sortedlist[i] + 1 == sortedlist[i+1]:
                count += 1
                longest = max(longest, count)
            else:
                count = 1
        if not nums:
            return 0
        return longest
                
            
                
            