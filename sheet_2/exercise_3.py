#! -*- coding:utf-8 -*-
import math
import numpy as np
import matplotlib.pyplot as plt

scan = np.loadtxt('laserscan.dat')
angle = np.linspace(-math.pi/2,math.pi/2,np.shape(scan)[0],endpoint='true')

ax = plt.subplot(111,projection='polar')
ax.plot(angle,scan,color='r')
ax.grid(True)
plt.show()