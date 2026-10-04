class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        hashmap ={}
       
        for i, num in enumerate(numbers):
            hashmap[num] = i
        for i in range (len(numbers)):
            needed = target - numbers[i]
            if needed in hashmap and i != hashmap[needed]:
                if hashmap[needed] + 1 > i+1:
                    return [i+1,hashmap[needed]+1 ] 
                else:
                    return [hashmap[needed]+1,i+1 ] 
                
        