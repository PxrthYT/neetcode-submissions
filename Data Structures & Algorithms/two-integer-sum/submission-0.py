class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        summing = {}
        for i in range (0,len(nums)):
            needed = target - nums[i]
            if needed in summing:
                return [summing[needed] , i]
            summing[nums[i]] = i
            

