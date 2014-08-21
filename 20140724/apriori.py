# -*- coding: utf-8 -*-


def loadDataSet(txt):
    item=[]
    for line in txt:
        line_clean=line.split()
        item.append(line_clean)
    return item

def createC1(dataSet):#产生单个item的集合
    C1=[]
    for transaction in dataSet:
        for item in transaction: 
            if not [item] in C1:
                C1.append([item])
    
    C1.sort()
    
    return map(frozenset,C1)#给C1.list每个元素执行函数
    
    
def scanD(D,ck,minSupport):#dataset,a list of candidate set,最小支持率
    ssCnt={}
    for tid in D:
        for can in ck:
            if can.issubset(tid):
                if can not in ssCnt:
                    ssCnt[can]=1
                else: ssCnt[can]+=1
    count=0
    for word in D:
        count+=1
    if count!=0:
        numItem=float(count)
    else:
        numItem=1
    retList=[]
    supportData={}
    for key in ssCnt:
        support=ssCnt[key]/numItem
        if support>=minSupport:
            retList.insert(0,key)
            supportData[key]=support
            
    return retList,supportData#返回频繁k项集，相应支持度
        

def aprioriGen(Lk,k):#create ck(k项集)
    retList=[]
    lenLk=len(Lk)
    for i in range(lenLk):
        for j in range(i+1,lenLk):
            L1=list(Lk[i])[:k-2];L2=list(Lk[j])[:k-2]
            L1.sort();L2.sort()#排序
            if L1==L2:#比较i,j前k-1个项若相同，和合并它俩
                retList.append(Lk[i] | Lk[j])#加入新的k项集 | stanf for union
    return retList
    
    
def apriori(dataSet,minSupport):
    C1=createC1(dataSet)
    D=map(set,dataSet)
    L1,supportData=scanD(D,C1,minSupport)#利用k项集生成频繁k项集（即满足最小支持率的k项集）
    L=[L1]#L保存所有频繁项集
    
    k=2
    while(len(L[k-2])>0):#直到频繁k-1项集为空
        Ck=aprioriGen(L[k-2],k)#利用频繁k-1项集 生成k项集
        Lk,supK= scanD(D,Ck,minSupport)
        supportData.update(supK)#保存新的频繁项集与其支持度
        L.append(Lk)#保存频繁k项集
        k+=1
    return L,supportData#返回所有频繁项集，与其相应的支持率
        
    
def calcConf(freqSet,H,supportData,brl,minConf):
    prunedH=[]
    for conseq in H:#后件中的每个元素
        conf=supportData[freqSet]/supportData[freqSet-conseq]
        if conf>=minConf:
            print (freqSet-conseq,'-->',conseq,'conf:',conf)
            brl.append((freqSet-conseq,conseq,conf))#添加入规则集中
            prunedH.append(conseq)#添加入被修剪过的H中
        
    return prunedH

def rulesFromConseq(freqSet,H,supportData,brl,minConf):
     
    m=len(H[0])#H是一系列后件长度相同的规则，所以取H0的长度即可
    if (len(freqSet)>m+1):
        Hmp1=aprioriGen(H,m+1)
        Hmp1=calcConf(freqSet,Hmp1,supportData,brl,minConf)
        if (len(Hmp1)>1):
            rulesFromConseq(freqSet,Hmp1,supportData,brl,minConf)
            
def generateRules(L,supportData,minConf):
  
    bigRuleList=[]#存储规则
    for i in range(1,len(L)):
        for freqSet in L[i]:
            H1=[frozenset([item]) for item in freqSet]
            if(i>1):
                rulesFromConseq(freqSet,H1,supportData,bigRuleList,minConf)
            else:
                calcConf(freqSet,H1,supportData,bigRuleList,minConf)
    return bigRuleList


f=open("/home/alber/experiment/20140724/35opic_correlation_for_AR.txt",'r')
txt=f.readlines()

dataSet=loadDataSet(txt)

C1=createC1(dataSet)

D=map(set,dataSet)

L1,suppData0=scanD(D,C1,0.05)   #设定最小支持率

L,suppData=apriori(dataSet,0.05)

print (L)
rules=generateRules(L,suppData,minConf=0)  #设定最小置信度

print (rules)