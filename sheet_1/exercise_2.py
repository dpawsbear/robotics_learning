#! -*- coding:utf-8 -*-

import pylab
import numpy as np

def plot_data():
    X = np.linspace(-2*np.pi,2*np.pi,256,endpoint=True)
    pylab.plot(X,calc_f(X))
    pylab.show()


# f(x) = cos(x) * exp(x)
def calc_f(x):
    ret_val = np.cos(x) * np.exp(x)
    return ret_val

plot_data()


