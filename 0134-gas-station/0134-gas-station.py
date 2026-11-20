class Solution:
    def canCompleteCircuit(self, gas: list[int], cost: list[int]) -> int:
        tank = total_tank = start = 0

        for i in range(len(gas)):
            balance = gas[i] - cost[i]
            tank += balance
            total_tank += balance

            if tank < 0:
                tank = 0
                start = i + 1

        return start if total_tank >= 0 else -1