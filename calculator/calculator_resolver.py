## 因通过eval()函数，存在安全隐患，本程序中自行实现表达式解析器，支持复杂表达式的计算
## 自定义表达式解析器的实现步骤：
## 1. 词法分析：将输入的表达式转换为Token序列 Tokenization
## 2. 语法分析：根据Token序列，构建语法树 Parsing
## 3. 语法树求值：根据语法树，计算表达式的值 Evaluation
import re

# 词法分析：将输入的表达式转换为Token序列
def tokenize(expression):
    tokens = re.findall(r"\d+|\+|\-|\*|\/|\(|\)|\^", expression.replace(" ", ""))
    return tokens


# 语法分析：根据Token序列，构建语法树
# 解析器：生成抽象语法树 (AST)
def parse(tokens):
    def parse_expression():
        return parse_addition_subtraction()

    def parse_addition_subtraction():
        node = parse_multiplication_division()
        while tokens and tokens[0] in ('+', '-'):
            op = tokens.pop(0)
            right = parse_multiplication_division()
            node = (op, node, right)
        return node

    def parse_multiplication_division():
        node = parse_power()
        while tokens and tokens[0] in ('*', '/'):
            op = tokens.pop(0)
            right = parse_power()
            node = (op, node, right)
        return node

    def parse_power():
        node = parse_parentheses()
        while tokens and tokens[0] == '^':
            op = tokens.pop(0)
            right = parse_parentheses()
            node = (op, node, right)
        return node

    def parse_parentheses():
        if tokens[0] == '(':
            tokens.pop(0)  # remove '('
            node = parse_expression()
            if tokens[0] == ')':
                tokens.pop(0)  # remove ')'
            else:
                raise ValueError("Expected ')'")
            return node
        return parse_number()

    def parse_number():
        if tokens[0].isdigit():
            return int(tokens.pop(0))
        raise ValueError("Expected number")

    return parse_expression()

# 计算 AST
def evaluate(ast):
    if isinstance(ast, int):
        return ast
    op, left, right = ast
    left_val = evaluate(left)
    right_val = evaluate(right)
    if op == '+':
        return left_val + right_val
    elif op == '-':
        return left_val - right_val
    elif op == '*':
        return left_val * right_val
    elif op == '/':
        if right_val == 0:
            raise ValueError("Cannot divide by zero")
        return left_val / right_val
    elif op == '^':
        return left_val ** right_val
    

if __name__ == "__main__":
    expression = input("请输入算数表达式: ")
    tokens = tokenize(expression)
    ast = parse(tokens)
    result = evaluate(ast)
    print(f"{expression} 计算结果: ", result)