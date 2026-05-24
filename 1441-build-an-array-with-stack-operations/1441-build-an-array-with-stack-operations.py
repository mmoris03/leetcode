class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        pointer = 0
        stack = []
        op_reg = []
        for number in range(1, n + 1):
            if pointer == len(target):
                break
            
            stack.append(number)
            op_reg.append("Push")

            if number != target[pointer]:
                stack.pop()
                op_reg.append("Pop")
                pointer-=1
            
            pointer+=1
        
        return op_reg