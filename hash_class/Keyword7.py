# -*- coding: utf-8 -*-
"""

@author: yingwenjie

"""

import os
import jieba
import jieba.posseg as pseg
from jieba import analyse
from sklearn import feature_extraction
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.feature_extraction.text import CountVectorizer
import numpy as np
import re
import scipy
import json
def stopwordslist(filename):
    stopword = [line.strip() for line in open(filename,'r',encoding='utf-8').readlines()]
    return stopword
def vocab(filename):
    voc = [line.strip() for line in open(filename,'r',encoding='utf-8').readlines()]
    return voc
    
#对文档进行分词处
def fenci(file_name, topK=10, stopwords_flag = False, sFilePath = "../data/hash_data/segfile"):
    stopwords = []
    if stopwords_flag:
    	stopwords = stopwordslist('./bin/stopwords.utf8')
    if not os.path.exists(sFilePath) : 
        os.mkdir(sFilePath)
    wf = open(sFilePath+"/one_file","w")
    wf_orgin = open(sFilePath+"/one_file_orgin","w")
    i = 0
    with open(file_name) as f:
      for line in f:
         if "tnews" in file_name:
             nid,label,label_text,content1,content2 = line.split('_!_')#tnews
         if "thucnews" in file_name:
             if len(line.split('_!_')) !=4:
                 print(line)
                 continue
             label,label_text,content1,content2 = line.split('_!_')#thucnews
         if "inews" in file_name:
             label,pid,content1,content2 = line.split('_!_')#inews
         #sample = line.strip('\n')
         sample = content1 + content2
         sample = re.sub('[A-Za-z0-9\!\%\[\]\"\:\,\.\_\-]'," ",sample)
         
         #tfdif关键词
         tfidf = analyse.extract_tags
         seg_list = tfidf(sample, topK)

         result = []
         for seg in seg_list:
             seg = ''.join(seg.split())
             if (seg != '' and seg != "\n" and seg != "\n\n" and seg not in stopwords):
                result.append(seg)
         if result:
             res = '\t'.join(result) + "\n"
             res_orgin = line.strip() + "\t" + res
             wf.write(str(label) + "\t" + res)
             wf_orgin.write(str(label) + "\t" + res_orgin)

      wf.close()
      wf_orgin.close()
    return sFilePath+"/one_file"

#对两段文本进行分词处
def fenci2(file_name, topK=10, json_flag = 0,stopwords_flag = False, sFilePath = "../data/hash_data/segfile"):
    stopwords = []
    if stopwords_flag:
    	stopwords = stopwordslist('./bin/stopwords.utf8')
    if not os.path.exists(sFilePath) : 
        os.mkdir(sFilePath)
    wf = open(sFilePath+"/one_file","w")
    wf_orgin = open(sFilePath+"/one_file_orgin","w")
    i = 0

    with open(file_name) as f:
      for line in f:
         if json_flag == 1:
             line_json = json.loads(line)
             content1 = line_json.get("sentence1") 
             content2 = line_json.get("sentence2") 
             label = line_json.get("label") 
         else:
             content1,content2,label = line.strip("\n").split('\t')#inews
             content1 = re.sub('[A-Za-z0-9\!\%\[\]\"\:\,\.\_\-]'," ",content1)
             content2 = re.sub('[A-Za-z0-9\!\%\[\]\"\:\,\.\_\-]'," ",content2)
         
         #tfdif关键词
         tfidf = analyse.extract_tags
         seg_list1 = tfidf(content1, topK)
         seg_list2 = tfidf(content2, topK)

         result1 = []
         result2 = []
         for seg in seg_list1:
             seg = ''.join(seg.split())
             if (seg != '' and seg != "\n" and seg != "\n\n" and seg not in stopwords):
                result1.append(seg)
         for seg in seg_list2:
             seg = ''.join(seg.split())
             if (seg != '' and seg != "\n" and seg != "\n\n" and seg not in stopwords):
                result2.append(seg)
         if result1 or result2:
             res1 = '\t'.join(result1)
             res2 = '\t'.join(result2) + "\n"
             wf.write(str(label) + "_!_" + res1 + "_!_" + res2)

      wf.close()
    return sFilePath+"/one_file"

#读取已分词好的文档，进行TF-IDF计算
def Tfidf(seg_file, max_feat=5000, sFilePath = "../data/hash_data/tfidffile") :
    if not os.path.exists(sFilePath) : 
        os.mkdir(sFilePath)
    #voc = vocab("tag_set")
    batch = 1000000
    corpus = []  #存取文档的分词结果
    corpus_seg = []  #存取文档的分词结果
    label_seg = []  #存取文档的分词结果
    i = 0
    with open (seg_file) as f:
        for line in f:
            if len(line.strip()) == 0:
               continue
            line_list = line.strip('\n').split('\t')
            label_seg.append(line_list[0])
            del line_list[0]
            corpus.append("\t".join(line_list))
            corpus_seg.append(line_list)
    """
    统计和存储各个关键词出现的次数
    """
    tfidf_word_file = open(sFilePath + "/word_num",'w')
    keys_dict = {}
    for item in corpus_seg:
        for key in item:
            keys_dict.setdefault(key,0)
            keys_dict[key] += 1
    keys_list =  sorted(keys_dict.items(),key = lambda x:x[1], reverse = True)
    for key,value in keys_list:
        tfidf_word_file.write(str(key) + "\t" + str(value) + "\n")

    vectorizer = CountVectorizer(max_features=max_feat, lowercase=False)    
    #vectorizer = CountVectorizer(lowercase=False, vocabulary=voc)    
    transformer = TfidfTransformer()
    tfidf = transformer.fit_transform(vectorizer.fit_transform(corpus))
    samples = []
    for s in range(len(corpus)):
        rowsp = tfidf.getrow(s)
        rowsp = rowsp.tocoo()
        num = rowsp.nnz
        col_value_list = []
        for i in range(num):
            col_value = (str(rowsp.col[i]) + "|" + str(rowsp.data[i]))
            col_value_list.append(col_value)
        samples.append(str(label_seg[s]) + "\t" + "_".join(col_value_list))
    
    word = vectorizer.get_feature_names() #所有文本的关键???

    return samples

if __name__ == '__main__':
    file_name = sys.argv[1]
    topK = 10
    max_features = 5000
    seg_file,seg_file_orgin = fenci(file_name,topK)
    #seg_file = "./kmeans/one_file"
    #seg_file_orgin = "./kmeans/one_file_orgin"
    Tfidf(seg_file, seg_file_orgin, cluster_num, max_features)
    #kmeans_cluster("./code_metapath2vec/202011_zhengpai_houyan_muying","./code_metapath2vec/out_train/train.cac.w10.l10.txt")
