# -*- coding: utf-8 -*-
"""

@author: yingwenjie

"""
import os
import sys
import string
import numpy as np
import scipy.io
from Keyword7 import *

def get_word_hash():
	words = [] 
	with open('../data/hash_data/word_wiki128_thucnews.utf8','r') as f:
		for line in f:
			words.append(line.strip('\n'))	
	arg = scipy.io.loadmat('../data/hash_data/arg2_wiki_thucnews.mat128')
	logPX1_B1 = arg['logPX1_B1']
	bits = logPX1_B1.shape[0]
	logPX1_B1 = np.power(2,logPX1_B1)
	logPX1_B0 = arg['logPX1_B0']
	logPX1_B0 = np.power(2,logPX1_B0)
	logPX1_B1_B0 = (logPX1_B1 - logPX1_B0) / (logPX1_B1 + logPX1_B0) 
	logPX1_B1_B0_sign = np.zeros((logPX1_B1_B0.shape), dtype = int)
	logPX1_B1_B0_sign[logPX1_B1_B0 >= 0] = 1
	logPX1_B1_B0_sign[logPX1_B1_B0 < 0] = -1
	word2hash = {}
	for i in range(len(words)):
		word2hash[words[i]] = logPX1_B1_B0_sign[:,i]
	return word2hash

def get_word_vec():
	word2vec = {} 
	with open('../data/hash_data/sgns.wiki.word','r') as f:
		for line in f:
			line_list = line.strip().split(' ')
			if(len(line_list) < 301):
				continue
			word = line_list[0]
			del line_list[0]
			word2vec[word] = np.array(line_list,dtype=np.float)
		
	return word2vec

def word2sample_hash(seg_file,word2hash):
    samples = []
    #print(type(word2hash))
    #print(type(word2hash["中国"]))
    #print((word2hash["中国"].shape))
    #for ww in word2hash:
    #    print(str(ww) + "\t" + str(word2hash[ww]))
    non = np.zeros((word2hash["中国"].shape[0]),dtype=np.float)
    with open(seg_file) as f:
       for line in f:
           seg_list = line.strip('\n').split('\t')
           label = seg_list[0]
           del seg_list[0]
           code = np.zeros((word2hash["中国"].shape[0]),dtype=np.float)
           for word in seg_list:
               code += word2hash.get(word,non)
           samples.append(str(label) + "\t" + "_".join([str(i) for i in code]))
    return samples

def word2sample_vec(seg_file,word2vec):
    samples = []
    non = np.zeros((word2vec["中国"].shape[0]))
    with open(seg_file) as f:
       for line in f:
           seg_list = line.strip('\n').split('\t')
           label = seg_list[0]
           del seg_list[0]
           code = np.zeros((word2vec["中国"].shape[0]))
           for word in seg_list:
               code += word2vec.get(word,non)
           samples.append(str(label) + "\t" + "_".join([str(i) for i in code]))
    return samples

def word2sample_onehot(segfile, word_file):
   word_dict = {}
   i = 0 
   with open(word_file) as f:
        for line in f:
            word = line.strip("\n")
            word_dict[word] = i
            i+=1
   samples = []
   with open(seg_file) as f:
       for line in f:
           seg_list = line.strip('\n').split('\t')
           label = seg_list[0]
           del seg_list[0]
           code = []
           for seg in seg_list:
                   index = word_dict.get(seg,-1) 
                   if index != -1:
                       code.append(index)
           samples.append(str(label) + "\t" + "_".join([str(i) for i in code]))
   return samples

if __name__ == '__main__':
    file_name = sys.argv[1]
    rep_type = sys.argv[2]
    data_type = sys.argv[3]
    topK = 10
    max_features = 100000
    label_flag = 0
    if data_type == "thucnews" or data_type == "inews":
         topK = 50
    if data_type == "tnews":
       label_flag = 1
    
    if(rep_type=="onehot"):
        seg_file = fenci(file_name,topK)
        samples = word2sample_onehot(seg_file,"../data/hash_data/word_wiki128.utf8")

    if(rep_type=="tfidf"):
        seg_file = fenci(file_name,topK) #tfidf需要训练、测试、验证集一起输进去，再拆分
        samples = Tfidf(seg_file, max_features)
    
    if(rep_type=="hash"):
        seg_file = fenci(file_name,topK)
        word2hash = get_word_hash()
        samples = word2sample_hash(seg_file,word2hash)

    if(rep_type=="word2vec"):
        word2vec = get_word_vec()
        seg_file = fenci(file_name,topK)
        samples = word2sample_vec(seg_file,word2vec)

    for ss in samples:
        if label_flag == 1:
            label_x = ss.strip('\n').split("\t")
            label = label_x[0]
            x = label_x[1]
            if int(label) <= 104:
                 label = int(label) - 100
            if int(label) > 105 and int(label) < 111:
                 label = int(label) - 101
            if int(label) > 111:
                 label = int(label) - 102
            print(str(label) + "\t" + str(x))
        else:
            print(ss)
