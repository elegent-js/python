# 最简易的计算器，只支持加减乘除四则运算，不支持括号，不支持负数
# 控制台计算器，没有UI

def calculator():
    print("欢迎使用简易计算器, 选择操作：")
    print("0. 退出")
    print("1. 加法")
    print("2. 减法")
    print("3. 乘法")
    print("4. 除法")
    
    choice = input("请输入操作编号(0/1/2/3/4)：")
    if choice == "0":
        print("退出计算器")
        return
    
    if choice not in ["1", "2", "3", "4"]:
        print("输入错误，请重新输入")
        calculator()
        return

    num1 = float(input("请输入第一个数："))
    num2 = float(input("请输入第二个数："))

    if choice == "1":
        print(f"{num1} + {num2} = {add(num1, num2)}")
    elif choice == "2":
        print(f"{num1} - {num2} = {sub(num1, num2)}")
    elif choice == "3":
        print(f"{num1} * {num2} = {mul(num1, num2)}")
    elif choice == "4":
        print(f"{num1} / {num2} = {div(num1, num2)}")
    else:
        print("输入错误，请重新输入")

    calculator()

# 加法
def add(num1, num2):
    return num1 + num2

# 减法
def sub(num1, num2):
    return num1 - num2

# 乘法
def mul(num1, num2):
    return num1 * num2

# 除法
def div(num1, num2):
    if num2 == 0:
        return "除数不能为0"
    return num1 / num2

if __name__ == "__main__":
    calculator()