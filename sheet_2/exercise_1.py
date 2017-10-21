#! -*- coding:utf-8 -*-
# 学习python 矩阵运算
# 实际应用是矩阵位置变换
import numpy as np

# G1原始坐标矩阵
G1 = np.array([[0,1,0,2],[1,0,0,6],[0,0,-1,2],[0,0,0,1]])
G1 = np.mat(G1)

# 旋转弧度
a1 = np.pi/2

# Z轴旋转矩阵T1
T1 = np.array([[np.cos(a1),-np.sin(a1),0,0],[np.sin(a1),np.cos(a1),0,0],[0,0,1,0],[0,0,0,1]])
T1 = np.mat(T1)

#算子左乘：表示点的平移是相对固定坐标系进行的坐标变换。
G2 = T1*G1
#算子右乘：表示点的平移是相对动坐标系进行的坐标变换。
G3 = G1*T1

print(G1,'\n\n',T1,'\n\n',G2,'\n\n',G3,'\n\n')


# 已知坐标系中点U的位置矢量 u=[7 3 2 1]T，将此点绕Z轴旋转90°，再绕Y轴旋转90°，求旋转后所得点W
# w = Rot(Y,90°)*Rot(Z,90°)*u

U = np.array([[7],[3],[2],[1]])
U = np.mat(U)

T2 = np.array([[np.cos(a1),0,np.sin(a1),0],[0,1,0,0],[-np.sin(a1),0,np.cos(a1),0],[0,0,0,1]])
T2 = np.mat(T2)
print('T2=',T2,'\n\n')

T4 = np.array([[0,0,1,0],[0,1,0,0],[-1,0,0,0],[0,0,0,1]])
T4 = np.mat(T4)

T3 = np.array([[0,-1,0,0],[1,0,0,0],[0,0,1,0],[0,0,0,1]])
T3 = np.mat(T3)

W = T2*T1*U
W2 = T4*T3*U
print('W=',W,'\n\n\n')
print('W2= ',W2,'\n\n\n')