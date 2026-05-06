class Solution(object):
    def longestSubsequence(self, arr, diff):
        """
        :type arr: List[int]
        :type difference: int
        :rtype: int
        """
        max_l=1
        d={}
        for i in arr:
            if i-diff in d:
                d[i]=d[i-diff]+1
            else:
                d[i]=1
            max_l=max(max_l,d[i])
        return max_l
            