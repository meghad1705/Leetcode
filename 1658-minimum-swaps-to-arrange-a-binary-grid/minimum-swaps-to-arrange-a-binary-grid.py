class Solution:
    def minSwaps(self, grid):
        n = len(grid)

        # Step 1 : count trailing zeros
        trailing = []

        for row in grid:
            count = 0
            for x in reversed(row):
                if x == 0:
                    count += 1
                else:
                    break
            trailing.append(count)

        swaps = 0

        # Step 2 : place correct row at each position
        for i in range(n):

            required = n - 1 - i

            j = i

            # find row with enough zeros
            while j < n and trailing[j] < required:
                j += 1

            # not found
            if j == n:
                return -1

            # bring row upward using swaps
            while j > i:
                trailing[j], trailing[j-1] = trailing[j-1], trailing[j]
                swaps += 1
                j -= 1

        return swaps
