#coding=utf-8
import sqlite3
db3=sqlite3.connect("./database/"+str(1)+"/SpiderResult.db3")
cu =db3.cursor()
a=cu.execute("select 评分,评论内容 from Content")
count=0
f=open("./data/product1.txt",'w')
for line in a:
    f.write(str(line[1])+"\n")


