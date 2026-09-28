class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = []
        hashmap = {}
        for i in range (len(strs)):
            sortedword = "".join(sorted(strs[i]))
            if sortedword in hashmap:
                hashmap[sortedword].append(strs[i])
            else:
                    hashmap[sortedword] = [strs[i]]
        for value in hashmap.values():
            result.append(value)
        return result
