class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operators = {
            '+': lambda a, b: a + b,
            '-': lambda a, b: a - b,
            '*': lambda a, b: a * b,
            '/': lambda a, b: int(a / b)  # truncates toward zero (not floor division)
        }
        stack = []
        for token in tokens:
            if token in operators:
                b, a = stack.pop(), stack.pop()  # order matters: a op b
                stack.append(operators[token](a, b))
            else:
                stack.append(int(token))  # cast once on push
        return stack[0]