#encoding=utf-8
import sys

a=["a","b","c"]
b=["b","c","d"]
dict_word={}
dict_word[a[0]]=a
dict_word[b[0]]=b
print (dict_word)
for i in range(10):
	for key in dict_word:
		if "d" in dict_word[key]:
			print ("yes")
			break
		else:
			print ("no")