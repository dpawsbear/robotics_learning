#! -*-coding:utf-8 -*-

import math as mh
from sympy import integrate,cos,sin
from sympy.abc import t


# 差速器模式
# 老位置按照指定参数运算出新位置
# 两种特殊情况，
# 1.当 v_r = v_l 时候，直线行走
# 2.当 v_r = -v_l 时候，原地转圈

def diffdrive(x_o,y_o,theta_o,v_l,v_r,i_t,l):
    # 第一种情况十分直线行走时候
    if (v_r - v_l <= 0.000001) and (v_r - v_l >= -0.000001):
        print('直线行走')
        v   = (v_r + v_l) / 2
        x_n = x_o + v * mh.cos(theta_o) * i_t
        y_n = y_o + v * mh.sin(theta_o) * i_t
        theta_n = theta_o
    else:
        w = (v_r - v_l) / l
        # 第二种情况，原地转圈
        if (v_r + v_l >= -0.000001) and (v_r+v_l <= 0.000001):  # 可能这种对比在浮点数上没有意义
            print('原地转圈')
            x_n = x_o
            y_n = y_o
            theta_n = theta_o + integrate(w*t,(t,0,i_t))
        else:
            print('正常行走')
            v = (v_r + v_l) / 2
            x_n = x_o + integrate(v*cos(w*t),(t,0,i_t))
            y_n = y_o + integrate(v*sin(w*t),(t,0,i_t))
            theta_n = theta_o + integrate(w*t,(t,0,i_t))

    return x_n,y_n,theta_n


x_o = 1.5
y_o = 2.0
theta_o = mh.pi/2

# c1 = (v_l=0.3m/s,v_r= 0.3m/s,t=3s)
x_n,y_n,theta_n = diffdrive(x_o,y_o,theta_o,0.3,0.3,3,0.5)
print('x_n= %fm y_n= %fm Θ_n=%f'%(x_n,y_n,theta_n))

# c2 = (v_l=0.1m/s,v_r=-0.1m/s,t=1s)
x_n,y_n,theta_n = diffdrive(x_n,y_n,theta_n,0.1,-0.1,3,0.5)
print('x_n= %fm y_n= %fm Θ_n=%f'%(x_n,y_n,theta_n))

# c3 = (v_l=0.3m/s,v_r= 0.0m/s,t=2s)
x_n,y_n,theta_n = diffdrive(x_n,y_n,theta_n,0.3,0.0,3,0.5)
print('x_n= %fm y_n= %fm Θ_n=%f'%(x_n,y_n,theta_n))

