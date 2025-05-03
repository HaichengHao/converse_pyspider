"""
@File    :拉格朗日乘数法.py
@Editor  : 百年
@Date    :2025/5/3 12:35 
"""
from scipy.optimize import minimize
import numpy as np

def objective(p):
    x, y = p
    return x**2 + y**2

def constraint(p):
    x, y = p
    return x + y - 1

# 初始猜测值
x0 = [0, 0]

# 设置约束
cons = [{'type': 'eq', 'fun': constraint}]

# 优化
res = minimize(objective, x0, method='SLSQP', constraints=cons)

print("最优解:", res.x)
print("最小值:", res.fun)