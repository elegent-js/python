## 复杂一些的计算器，还是没有UI，但支持复杂表达式的计算
## 例如：(1+2)*3-4/2
## 但需要注意：采用eval()函数，存在安全隐患，不要随便输入表达式

def calculator():
    expression = input("请输入算数表达式: ")

    try:
        result = eval(expression)
        print(f"{expression} 计算结果: ", result)
    except Exception as e:
        print("表达式错误：", e)
        return
    
if __name__ == "__main__":
    calculator()