import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import math
from getReqTimeDate import *


# 正态分布的概率密度函数。可以理解成 x 是 mu（均值）和 sigma（标准差）的函数
def normfun(x, mu, sigma):
    pdf = np.exp(-((x - mu) ** 2) / (2 * sigma ** 2)) / (sigma * np.sqrt(2 * np.pi))
    return pdf


mu = 5915.193548
sigma = 506.241933
# Python实现正态分布
# 绘制正态分布概率密度函数
x = np.linspace(mu - 3 * sigma, mu + 3 * sigma, 50) # 根据3σ原则求等差数列 作为x轴
y_sig = np.exp(-(x - mu) ** 2 / (2 * sigma ** 2)) / (math.sqrt(2 * math.pi) * sigma)
plt.plot(x, y_sig, "r-", linewidth=2)
plt.vlines(mu, 0, np.exp(-(mu - mu) ** 2 / (2 * sigma ** 2)) / (math.sqrt(2 * math.pi) * sigma), colors="c",
           linestyles="dashed")
plt.vlines(mu + sigma, 0, np.exp(-(mu + sigma - mu) ** 2 / (2 * sigma ** 2)) / (math.sqrt(2 * math.pi) * sigma),
           colors="k", linestyles="dotted")
plt.vlines(mu - sigma, 0, np.exp(-(mu - sigma - mu) ** 2 / (2 * sigma ** 2)) / (math.sqrt(2 * math.pi) * sigma),
           colors="k", linestyles="dotted")
plt.xticks([mu - sigma, mu, mu + sigma], ['μ-σ', 'μ', 'μ+σ'])
# plt.xticks([mu - 2 * sigma, mu, mu + 2 * sigma], ['μ-2σ', 'μ', 'μ+2σ'])
# plt.xticks([mu - 3 * sigma, mu, mu + 3 * sigma], ['μ-3σ', 'μ', 'μ+3σ'])
plt.xlabel('ReqTime')
plt.ylabel('Latent Trait')
plt.title('Normal Distribution: $\mu = %.2f, $sigma=%.2f' % (mu, sigma))
plt.grid(True)
plt.show()