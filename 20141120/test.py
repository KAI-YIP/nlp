#coding=utf-8
import numpy as np

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
    noun_topic={}
    for i in range(len(noun)):
        noun_topic[noun[i]]=topic_list[i]
    return noun_topic

def KL_dis(KL_distribution1,KL_distribution2):
    """计算两分布间的KL距离"""
    C_entropy1=0
    C_entropy2=0
    for i in range(len(KL_distribution1)):
        temp1=float(KL_distribution1[i])*np.log10(float(KL_distribution2[i]))
        C_entropy1+=temp1
        temp2=float(KL_distribution2[i])*np.log10(float(KL_distribution1[i]))
        C_entropy2+=temp2
    return -C_entropy1,-C_entropy2

def cosine(cosine_distribution1,cosine_distribution2):
    """计算两分布间的余弦相似度"""
    XIYI=0
    squarX=0
    squarY=0
    for i in range(len(cosine_distribution1)):
        temp1=float(cosine_distribution1[i])*float(cosine_distribution2[i])
        XIYI+=temp1
        squarX+=(float(cosine_distribution1[i]))*(float(cosine_distribution1[i]))
        squarY+=(float(cosine_distribution2[i]))*(float(cosine_distribution2[i]))
    similarity=XIYI/((np.sqrt(squarX))*(np.sqrt(squarY)))
    return similarity

matrix=readmatrix()
similar_dict={}
for k1 in matrix:
    for k2 in matrix:
        if k1!=k2:
            zuheci1=tuple([k1,k2])
            zuheci2=tuple([k2,k1])
            similarity1,similarity2=KL_dis(matrix[k1],matrix[k2])
            similar_dict[zuheci1]=similarity1
            similar_dict[zuheci2]=similarity2
        else:
            pass
h=open("./名词的交叉熵.txt",'w')
for k,v in sorted(similar_dict.items(),key=lambda d:d[1],reverse=True):
    h.write(str(k[0])+" "+str(k[1])+" "+str(v)+"\n")



