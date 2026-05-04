class Solution(object):
    def spiralOrder(self, arr):
        res=[]
        t=l=0
        r=len(arr[0])-1 #last col
        b=len(arr)-1 #last row
        while l<=r and t<=b:
            for j in range(l,r+1):
                res.append(arr[t][j])
            t+=1
            for i in range(t,b+1):
                res.append(arr[i][r])
            r-=1
            if t<=b:
                for k in range(r,l-1,-1):
                    res.append(arr[b][k])
                b-=1
            if l<=r:
                for i in range(b,t-1,-1):
                    res.append(arr[i][l])
                l+=1
        return res