#coding=utf-8
import matplotlib
matplotlib.use('Agg')

import matplotlib.pyplot as plt
import numpy as np


class draw:
    """将topic的变化可视化"""
    def readmatrix(readmatrix_trace_noun="./名词集合.txt",readmatrix_trace_topic="./主题分布.txt"):
        """读取名词以及名词的语义分布存为数组"""
        f1=open(readmatrix_trace_noun,'r')
        noun=[]
        for line in f1.readlines():
            line_clean=line.split()
            noun.append(line_clean[0])
        topic_list=[]
        f2=open(readmatrix_trace_topic,'r')
        for line in f2.readlines():
            line_clean=line.split()
            topic_list.append(line_clean)
        noun_topic=[]
        for i in range(len(noun)):
            temp_list=[noun[i],topic_list[i]]
            noun_topic.append(temp_list)
        return noun_topic

    def picture_topic(picture_topic_distribution,picture_topic_name):
        """做主题分布条行图"""
        y=[]
        for number in picture_topic_distribution:
            y.append(float(number))
        fig,ax= plt.subplots()
        x=range(len(y))
        plt.title(str(picture_topic_name))
        plt.xlabel("topic")
        plt.ylabel("概率")
        plt.bar(x,y,alpha=0.7, color='b')
        plt.ylim(0,0.1)
        plt.tight_layout()
        plt.savefig("./noun/"+str(picture_topic_name)+".png")
        plt.plot()
        print ("figure"+str(picture_topic_name)+".png has been saved")

if __name__=="__main__":
    matrix=draw.readmatrix()
    print (matrix[169])
    for word in matrix:
        word_clean=word[0].split("/")
        name=word_clean[0]
        draw.picture_topic(word[1],str(name))

