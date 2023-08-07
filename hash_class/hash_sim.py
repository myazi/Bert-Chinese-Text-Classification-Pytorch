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

def cal_sim(code1,code2):
	if len(code1) != len(code2):
		return inf
	score = 0
	return np.dot(code1.T,code2)

def cal_sim_onehot(code1,code2):
	score = 0
	for c1 in code1:
		if c1 in code2:
			score +=1
	return score

def get_word_hash():
	words = [] 
	with open('../data/hash_data/word_wiki128.utf8','r') as f:
		for line in f:
			words.append(line.strip('\n'))	
	arg = scipy.io.loadmat('../data/hash_data/arg2_wiki.mat128')
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
           label,seg1,seg2 = line.strip('\n').split('_!_')
           seg_list1 = seg1.strip('\n').split('\t')
           seg_list2 = seg2.strip('\n').split('\t')
           code1 = np.zeros((word2hash["中国"].shape[0]),dtype=np.float)
           code2 = np.zeros((word2hash["中国"].shape[0]),dtype=np.float)
           for word in seg_list1:
               code1 += word2hash.get(word,non)
           for word in seg_list2:
               code2 += word2hash.get(word,non)
           code11 = np.zeros((code1.shape), dtype = int)
           code22 = np.zeros((code2.shape), dtype = int)
           code11[code1 >= 0] = 1
           code11[code1 < 0] = -1
           code22[code2 >= 0] = 1
           code22[code2 < 0] = -1
           score = cal_sim(code1,code2)
           samples.append(str(label) + "\t" + str(score) + "\t" + "_".join([str(i) for i in code1]) + "\t" + "_".join([str(i) for i in code2]))
    return samples

def word2sample_vec(seg_file,word2vec):
    samples = []
    non = np.zeros((word2vec["中国"].shape[0]))
    with open(seg_file) as f:
       for line in f:
           label,seg1,seg2 = line.strip('\n').split('_!_')
           seg_list1 = seg1.strip('\n').split('\t')
           seg_list2 = seg2.strip('\n').split('\t')
           code1 = np.zeros((word2vec["中国"].shape[0]))
           code2 = np.zeros((word2vec["中国"].shape[0]))
           for word in seg_list1:
               code1 += word2vec.get(word,non)
           for word in seg_list2:
               code2 += word2vec.get(word,non)
           score = cal_sim(code1,code2)
           samples.append(str(label) + "\t" + str(score) + "\t" + "_".join([str(i) for i in code1]) + "\t" + "_".join([str(i) for i in code2]))
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
           label,seg1,seg2 = line.strip('\n').split('_!_')
           seg_list1 = seg1.strip('\n').split('\t')
           seg_list2 = seg2.strip('\n').split('\t')
           code1 = []
           code2 = []
           for seg in seg_list1:
                   index = word_dict.get(seg,-1) 
                   if index != -1:
                       code1.append(index)
           for seg in seg_list2:
                   index = word_dict.get(seg,-1) 
                   if index != -1:
                       code2.append(index)
           score = cal_sim(code1,code2)
           samples.append(str(label) + "\t" + str(score) + "\t" + "_".join([str(i) for i in code1]) + "\t" + "_".join([str(i) for i in code2]))
   return samples

if __name__ == '__main__':
    file_name = sys.argv[1]
    rep_type = sys.argv[2]
    data_type = sys.argv[3]
    topK = 1000
    max_features = 100000
    json_flag = 0
    if data_type == "afqmc":
        json_flag = 1
    if(rep_type=="onehot"):
        seg_file = fenci2(file_name,topK,json_flag)
        samples = word2sample_onehot(seg_file,"../data/hash_data/word_wiki128.utf8")

    if(rep_type=="tfidf"):
        seg_file = fenci2(file_name,topK,json_flag) #tfidf需要训练、测试、验证集一起输进去，再拆分
        samples = Tfidf(seg_file, max_features)
    
    if(rep_type=="hash"):
        seg_file = fenci2(file_name,topK,json_flag)
        word2hash = get_word_hash()
        samples = word2sample_hash(seg_file,word2hash)

    if(rep_type=="word2vec"):
        word2vec = get_word_vec()
        seg_file = fenci2(file_name,topK,json_flag)
        samples = word2sample_vec(seg_file,word2vec)
    for ss in samples:
        print(ss)
