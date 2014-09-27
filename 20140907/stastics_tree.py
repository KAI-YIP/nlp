# -*- coding: UTF-8-*-
import matplotlib.pyplot as plt
import numpy as np


class TopicTree:
	"""统计层次聚类树层次的变化情况"""

	def openfile(open_trace="./tplink/相似度阈值0.01/topic_tree.txt"):
		"""打开tree并统计每一类的长度"""
	
		len_openfile=[]
		f=open(open_trace,'r')
		for line in f.readlines():
			line_clean=line.split()
			if (len(line_clean))<=2:
				pass
			else:
				len_openfile.append(len(line_clean))
		return len_openfile
	
if __name__ == '__main__':
	name_list=[0,0.05,0.1,0.15,0.2]
	for name in name_list:
		plt.figure(name)
		plt.title("类数量的下降:相似度阈值"+str(name))
		plt.xlabel("迭代层数")
		plt.ylabel("类数量")
		len_topic1=TopicTree.openfile("./tplink/相似度阈值"+str(name)+"/topic_tree.txt")
		len_topic2=TopicTree.openfile("./iphone5s/相似度阈值"+str(name)+"/topic_tree.txt")
		plt.plot(len_topic1)
		plt.plot(len_topic2)
		plt.savefig('./类数量下降图/相似度阈值'+str(name)+'.png')