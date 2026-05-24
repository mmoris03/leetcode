class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        _add = lambda a, b: a + b
        _sub = lambda a, b: a - b
        _mul = lambda a, b: a * b
        _div = lambda a, b: int(float(a) / b)
        
        op_to_func = {
            "+": _add,
            "-": _sub,
            "*": _mul,
            "/": _div,
        }
        
        stack = []
        for token in tokens:
            if token in op_to_func:
                b = stack.pop()
                a = stack.pop()
                value = op_to_func[token](a, b)
            else:
                value = int(token)
            
            stack.append(value)
        return stack.pop()
        