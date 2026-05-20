"""
test.py - 示例文件
功能：演示如何解决Pylint提示
"""

def calculate_sum(num_list):
    """计算列表数字的总和"""
    total = 0
    for num in num_list:
        total += num
    return total


# 测试函数
print(calculate_sum([1, 2, 3]))  # 输出: 6