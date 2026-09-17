class Solution:
    def validPalindrome(self, s: str) -> bool:
        def palindrome(s): 
            l = 0 
            r = len(s) - 1 
            while l < r: 
                if s[l] == s[r]: 
                    l += 1 
                    r -= 1 
                else:
                    return False
            return True
        if palindrome(s) == True: 
            return True 
        for i in range(len(s)): 
            new_s = s[:i] + s[i + 1:]
            if palindrome(new_s) == True: 
                return True
        return False