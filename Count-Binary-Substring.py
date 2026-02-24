class Solution:
    def countBinarySubstrings(self, s):

        groups = []
        count = 1
        
        # count consecutive characters
        for i in range(1, len(s)):
            if s[i] == s[i-1]:
                count += 1
            else:
                groups.append(count)
                count = 1
        
        groups.append(count)
        
        result = 0
        
        # compare adjacent groups
        for i in range(1, len(groups)):
            result += min(groups[i], groups[i-1])
        
        return result
