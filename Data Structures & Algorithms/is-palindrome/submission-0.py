class Solution:
    def isPalindrome(self, s: str) -> bool:
        stringfinal=""
        for char in s:
            if char.isalnum():
                stringfinal += char.lower()
        left = 0
        right = len(stringfinal) - 1
        while left < right:
            if stringfinal[left] == stringfinal[right]:
                left += 1
                right -= 1
            else:
                return False
        return True    
        
            
        