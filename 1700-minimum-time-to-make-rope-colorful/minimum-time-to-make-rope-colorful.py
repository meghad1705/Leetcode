class Solution(object):
    def minCost(self, colors, neededTime):
        total_cost = 0
        max_time = neededTime[0]

        for i in range(1, len(colors)):
            if colors[i] == colors[i - 1]:
                total_cost += min(max_time, neededTime[i])
                max_time = max(max_time, neededTime[i])
            else:
                max_time = neededTime[i]

        return total_cost
