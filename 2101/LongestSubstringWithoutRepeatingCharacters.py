class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        substrings = []
        m = 0
        
        for i in range(len(s)):
            substring = s[i]
            for j in range(i + 1, len(s)):
                if not s[j] in substring:
                    substring += s[j]
                else:
                    break
            if len(substring) > m:
                m = len(substring)
                substrings.append(substring)
        return m
