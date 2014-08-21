# -*- coding: UTF-8-*-
import numpy
import math
import string
import matplotlib.pyplot as plt
import re

def dictionary_found(wordlist):               
	word_dictionary1={}
	for i in list(range(len(wordlist))):
		if i%2==0:
			if wordlist[i] in word_dictionary1:
				word_probability=word_dictionary1.get(wordlist[i])
				word_probability=float(word_probability)+float(wordlist[i+1])
				word_dictionary1.update({wordlist[i]:word_probability})
			else:
				word_dictionary1.update({wordlist[i]:wordlist[i+1]})
		else:
			pass
	return word_dictionary1

def look_into_dic(dictionary,testset,iteration):
	'''Calculates the TF-list for perplexity'''	
	frequency=[]
	letter_list=[]
	a=0.0
	for letter in testset.split():
		if letter not in letter_list:
			letter_list.append(letter)
			letter_frequency=(dictionary.get(letter))
			frequency.append(letter_frequency)
		else:
			pass
	for each in frequency:
		if each!=None:
			a=a+math.log(float(each)/iteration)
		else:
			pass
	b=-a
	return b 

def f_testset_word_count(testset):
	'''reture the sum of words in testset which is the denominator of the formula of Perplexity'''
	testset_clean=testset.split()
	return (len(testset_clean)-testset.count("\n"))

def f_perplexity(word_frequency,word_count):
	'''Search the probability of each word in dictionary
	Calculates the perplexity of the LDA model for every parameter T'''
	duishu=word_frequency
	kuohaoli=duishu/word_count
	perplexity=math.exp(kuohaoli)
	return perplexity

def graph_draw(topic,perplexity):
	x=topic
	y=perplexity
	plt.plot(x,y,color="red",linewidth=2)
	plt.xlabel("Number of Topic")
	plt.ylabel("Perplexity")
	plt.show()


topic=[]
perplexity_list=[]
f1=open('/home/alber/experiment/20140721/dell_test.txt','r')
testset=f1.read()
testset_word_count=f_testset_word_count(testset)		 #call the function to count the sum-words in testset
for i in list(range(19)):
	dictionary={}
	iteration=(5*i+10)
	topic.append(iteration)
	trace="./lda/model-final-"+str(iteration)+".txt"
	f=open(trace,'r')
	text=f.readlines()
	word_list=[]
	for line in text:
		if "Topic" not in line:
			line_clean=line.split()
			word_list.extend(line_clean)	
		else:
			pass
	word_dictionary=dictionary_found(word_list)
	frequency=look_into_dic(word_dictionary,testset,iteration)
	perplexity=f_perplexity(frequency,testset_word_count)
	perplexity_list.append(perplexity)		
graph_draw(topic,perplexity_list)