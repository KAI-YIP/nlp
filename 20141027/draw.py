#coding=utf-8
import matplotlib
matplotlib.use('Agg')

import matplotlib.pyplot as plt
import numpy as np


class draw:
	"""将topic的变化可视化"""

	def readmatrix(readmatrix_trace="./topic_line/topic_line1.txt"):
		"""将个时间段的topic分布读取为数组"""
		matrix={}
		f=open(readmatrix_trace,'r')
		j=0
		for line in f.readlines():
			topid_dict={}
			line_clean=line.split()
			for i in range(len(line_clean)):
				topid_dict[i]=line_clean[i]
			matrix[j]=topid_dict
			j+=1
		return matrix

	def picture_topic(picture_topic_matrix,picture_topic_number):
		"""对于给定的topic，做topic在时间上的变化图"""
		x_name=[]
		y=[]
		for k in sorted(picture_topic_matrix.keys()):
			x_name.append(k)
			y.append(picture_topic_matrix[k][picture_topic_number])
		x=np.arange(len(y))
		fig, ax = plt.subplots()
		plt.title("Topic"+str(picture_topic_number)+" 随时间变化图")
		plt.xlabel("201401-201407/15天")
		plt.ylabel("概率")
		plt.plot(x,y,alpha=0.8,color="red",label="Topic-"+str(picture_topic_number))
		plt.xticks(x,x_name)
		plt.legend()
		plt.savefig("./topic_line/topic_line2/topic_dis"+str(picture_topic_number)+".png")
		plt.plot()	
		print ("figure"+str(picture_topic_number)+".png has been saved")

	def picture_times(picture_times_matrix,picture_times_number):
		"""对于给定的时间段，做该时间段的topic分布图"""
		x=[]
		y=[]
		tempdict=picture_times_matrix[picture_times_number]
		for k in sorted(tempdict):
			x.append(k)
			y.append(float(tempdict[k]))
		fig, ax = plt.subplots()
		x_name=np.arange(len(y))
		plt.title("在第"+str(picture_times_number)+" 个时间段的分布图")
		plt.xlabel("topic0-"+str(len(tempdict)-1))
		plt.ylabel("概率")
		plt.bar(x_name,y,0.9,alpha=0.7, color='b',label='topic'+str(picture_times_number))
		plt.xticks(x_name+0.5,x)
		plt.ylim(0,0.1)
		plt.tight_layout()
		plt.savefig("./topic_line/topic_line2/time_line"+str(picture_times_number)+".png")	
		plt.plot()
		print ("figure"+str(picture_times_number)+".png has been saved")



if __name__=="__main__":
	matrix=draw.readmatrix("./topic_line/topic_line1.txt")
	for i in range(len(matrix[0])):
		draw.picture_topic(matrix,i)
	for i in range(len(matrix)):
		draw.picture_times(matrix,i)
	

