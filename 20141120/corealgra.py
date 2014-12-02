#coding=utf-8
f=open("./huawei6.txt",'r')
content_f=f.readlines()
content=[]
for line in content_f:
    line_clean=line.split()
    if len(line_clean)>=2:
        content.append(" ".join(line_clean))
    else:
        pass
noun=[]
f=open("./名词词频统计.txt",'r')
for line in f.readlines():
    line_clean=line.split()
    noun.append(line_clean[0])

def find_affiliate(find_affiliate_word,find_affiliate_content):
    """生成名词附属文档,并返回新文档候选"""
    content=find_affiliate_content[:]
    new_content=[find_affiliate_word,""]
    for line in find_affiliate_content:
        line_clean=line.split()
        if find_affiliate_word in line_clean:
            new_content[1]+=" "+line
            content.remove(line)
        else:
            pass
    return new_content,content
word_affiliate_array=[]
for word in noun:
    if len(content)>=1 and word in " ".join(content):
        word_affiliate,new_content=find_affiliate(word,content)
        word_affiliate_array.append(word_affiliate)
        content=new_content
    else:
        break
f1=open("./名词及其附属词.txt",'w')
f2=open("./名词集合.txt",'w')
for line in word_affiliate_array:
    f2.write(line[0]+"\n")
    f1.write(line[1]+"\n")



