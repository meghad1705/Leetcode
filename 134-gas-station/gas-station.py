class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        if sum(gas)<sum(cost): # 15<16 15lit of gas to travel 16km 
            return -1
        g1=startind=0
        for i in range(len(gas)):
            g1=g1+gas[i]-cost[i]
            if g1<0:
                g1=0
                startind=i+1
        return startind
        