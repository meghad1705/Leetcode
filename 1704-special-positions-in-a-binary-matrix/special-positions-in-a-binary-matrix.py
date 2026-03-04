class Solution(object):
    def numSpecial(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: int
        """
        m = len(mat)
        n = len(mat[0])
        
    
        row_sum = [sum(row) for row in mat]
        col_sum = [0] * n
        for j in range(n):
            for i in range(m):
                col_sum[j] += mat[i][j]
                count = 0
        for i in range(m):
            for j in range(n):
                if mat[i][j] == 1 and row_sum[i] == 1 and col_sum[j] == 1:
                    count += 1
        
        return count