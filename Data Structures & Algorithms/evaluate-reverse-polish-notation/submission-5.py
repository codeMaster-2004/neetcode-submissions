class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operators = {
            '+': lambda a, b: int(a) + int(b),
            '-': lambda a, b: int(a) - int(b),
            '*': lambda a, b: int(a) * int(b),
            '/': lambda a, b: int(int(a) / (int(b)))  # Integer division
        }
        res = 0
        stack = []
        for i in range(len(tokens)):
            if (tokens[i] not in operators):
                stack.append(tokens[i])
                print(stack)
            else: 
                num1 = stack.pop()
                print(stack)
                num2 = stack.pop()
                print(stack)
                res = operators[tokens[i]](num2, num1)
                stack.append(res)
                print(stack)
        return int(stack[0])
