class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        cost.append(0)
        # zeroth, first = 0, 1
        cost1 = 0
        for i in range(len(cost) - 3, -1, -1):
            cost[i] = min(cost[i] + cost[i + 1], cost[i] + cost[i + 2])
            # if cost[i] + cost[i + 1] < cost[i] + cost[i + 2]:
            #     i = i + 1
            # else:
            #     i = i + 2

        return min(cost[0], cost[1])