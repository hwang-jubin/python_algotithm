# 

class Solution:
    def canCompleteCircuit(self, gas, cost):
        total_gas = 0
        total_cost = 0
        current_gas = 0
        start_index = 0

        for i in range(len(gas)):
            total_gas += gas[i]
            total_cost += cost[i]
            current_gas += gas[i] - cost[i]

            if current_gas < 0:
                # 현재 주유소에서 가스가 부족하므로 다음 주유소에서 출발
                start_index = i + 1
                current_gas = 0

        return start_index
solution = Solution()
print(solution.canCompleteCircuit(gas = [1,2,3,4,5], cost = [3,4,5,1,2]))