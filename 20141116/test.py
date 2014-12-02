#coding=utf-8
h=open("./data/result.txt",'w')
count=0
for i in range(10):
    i+=1
    f=open("./data/product"+str(i)+"sentence.txt",'r')
    for line in f.readlines():
        line_clean=" ".join(line.split())
        h.write(line_clean+"\n")
        count+=1
h.close()
h=open("./data/result.txt",'r')
f=open("/home/alber/lda/GibbsLDA/jd/N_product.txt",'a')
f.write(str(count)+"\n")
for line in h.readlines():
    f.write(line)
