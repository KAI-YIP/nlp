#coding=UTF-8
f=open("./data.txt",'r')
content=f.readlines()
f.close()
def exchange(s):
    up='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    ns=''
    for c in s:
        if c in up:
            ns+=c.lower()
        else:
            ns+=c
    return ns
h=open("./data.txt",'w')
for line in content:
    line_clean=line.split()
    for word in line_clean:
        new_word=exchange(word)
        h.write(new_word+" ")
    h.write("\n")

