class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n=len(nums)
        ans=[]
        num=set(nums)
        for i in range(1,n+1):
            if  i not in num:
                ans.append(i)
        return ans