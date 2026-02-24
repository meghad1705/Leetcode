class Solution(object):
    def binaryGap(self, n):
        
        b = bin(n)[2:]   # remove '0b'
        
        prev = -1
        max_dist = 0
        
        for i in range(len(b)):
            if b[i] == '1':
                if prev != -1:
                    max_dist = max(max_dist, i - prev)
                prev = i
        
        return max_dist

        
