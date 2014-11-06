#coding=utf-8
import numpy as np
import matplotlib.pyplot as plt


n_groups = 40

means_men = [20, 35, 30, 35, 27]
means_women =[0.017839,0.033129,0.006626,0.011723,0.020897,0.022936,0.001529,0.005607,0.056575,0.016820,0.011723,0.018858,0.013761,0.005607,0.003568,0.001529,0.000510,0.000510,0.001529,0.049439,0.011723,0.025994,0.000510,0.011723,0.000510,0.058614,0.004587,0.000510,0.025994,0.027013,0.004587,0.002548,0.024975,0.000510,0.021916,0.033129,0.004587,0.014781,0.008665,0.416412] 
fig, ax = plt.subplots()
index = np.arange(n_groups)
bar_width = 0.7
opacity = 0.9
plt.bar(index, means_women, bar_width,alpha=opacity, color='b',label='Men')
plt.xlabel('Group')
plt.ylabel('Scores')
plt.title('Scores by group and gender')
plt.xticks(index+bar_width/2, range(len(means_women)))
plt.ylim(0,0.1)
plt.legend()

plt.tight_layout()
plt.show()
