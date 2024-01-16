def calculate_sum(a, b):
    """
    计算两个数的和。

    参数：
    a -- 第一个加数
    b -- 第二个加数

    返回值：
    两个加数的和
    """
    return a + b

def main():
    num1 = int(input("请输入第一个数字： "))
    num2 = int(input("请输入第二个数字： "))

    result = calculate_sum(num1, num2)
    print(f"{num1} 和 {num2} 的和是： {result}")

if __name__ == "__main__":
    main()
