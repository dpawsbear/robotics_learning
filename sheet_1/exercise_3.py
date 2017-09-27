#! -*- coding:utf-8 -*-

import pylab
import numpy as np

def plot_data():

    #随机种子
    np.random.seed(123)

    #产生平均值为5，标准差为2，的正太分布随机数
    vector_a  = np.random.normal (5, 2, 100000)
    #产生0-10均匀分布的随机数
    vector_b  = np.random.uniform(0,10, 100000)

    #计算平均值
    mean_a = np.mean(vector_a)
    mean_b = np.mean(vector_b)
    print("mean_a: %f mean_b: %f" %(mean_a,mean_b))

    #计算标准差
    std_a = np.std(vector_a)
    std_b = np.std(vector_b)
    print("std_a : %f std_b : %f"%(std_a,std_b))

    #绘制直方图
    an, abin, apatches = pylab.hist(vector_a, bins=100, normed=0, facecolor='green')
    bn, bbin, bpatches = pylab.hist(vector_b, bins=100, normed=0, facecolor='red'  )
    pylab.show()

if __name__ == "__main__":
    plot_data()


