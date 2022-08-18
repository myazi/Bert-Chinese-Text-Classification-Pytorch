# coding: UTF-8
import time
import torch
import torch.nn as nn
import torch.nn.functional as F
import numpy as np
from train_eval import train, init_network
from importlib import import_module
import argparse
from utils import build_dataset, build_dataset_withtag, build_iterator, get_time_dif, build_iterator_1,build_iterator_n,  build_dataset_line, build_dataset_line_withtag
import os
import sys
import json

from rule import rule
os.environ["CUDA_VISIBLE_DEVICES"] = "6,7"
parser = argparse.ArgumentParser(description='Chinese Text Classification')
parser.add_argument('--model', type=str, required=True, help='choose a model: Bert, ERNIE')
args = parser.parse_args()

if __name__ == '__main__':
    dataset = '../data'
    model_name = args.model  # bert
    x = import_module('models.' + model_name)
    config = x.Config(dataset)
    np.random.seed(1)
    torch.manual_seed(1)
    torch.cuda.manual_seed_all(1)
    torch.backends.cudnn.deterministic = True  # 保证每次结果一样

    start_time = time.time()
    #print("Loading data...")
    model = x.Model(config).to(config.device)
    model = nn.DataParallel(model)
    model.load_state_dict(torch.load(config.save_path))
    model.eval()
    class_list = config.class_list
    """
    建立index2hangye 字典
    """
    index2hangye = {}
    for i in range(len(class_list)):
        index2hangye[i] = class_list[i].strip().split(" ")[1]
    
    i = 0
    test_datas = []
    line_list = []
    for line in sys.stdin:
        i += 1
        line = line.strip('\n').split("\t")        
        if len(line) < 3: continue
        nid = line[0]
        title = line[1]
        tag = line[9].replace("[","").replace("]","").replace(","," ").replace("\"","")

        #title = line[4]
        #stitle = line[31]
        #title+= stitle
        #tag = line[7].replace("|","").replace("]","").replace(","," ").replace("\"","")
        #stag = (line[36] + line[37] + line[38]).replace("/","")
        
        #if title.strip() == '':continue
        #print(str(title) + "\t" + str(tag)) 
        
        title_tag = '\t'.join([title, tag, "0"])
        test_data = build_dataset_line_withtag(config, title_tag)
        test_datas.append(test_data[0])
        line_list.append(line)
        if i % 1000 == 0:
           #print(str(title_tag) + "\t" + str(i))
           test_iter = build_iterator_n(test_datas,len(test_datas),config)
           with torch.no_grad():
                for texts, labels in test_iter:
                    outputs = model(texts)
                    #print(outputs)
                    ttt = F.softmax(outputs)
                    #print(ttt)
                    predic = torch.max(outputs.data, 1)[1].cpu().numpy()
                    softmax = torch.max(ttt.data, 1)[0].cpu().numpy()
                    othor_index = len(class_list) - 1 
                    for i in range(len(softmax)):
                        if softmax[i] < 0.2:
                           predic[i] = othor_index
                        #if softmax[i] < 0.8:
                        #predic[i] = rule(predic[i],str(line_list[i][0] + line_list[i][1]),index2hangye)
                        #predic[i] = rule(predic[i],str(line_list[i][1]))
                        #predic[i] = rule2(predic[i],line_list[i][0])
                    #predic = torch.max(outputs.data, 1)[1].cpu().numpy()
                    #print(outputs.data)
                    #print(torch.max(outputs.data, 1))
                    sss = torch.sort(ttt.data, 1, descending=False)[1].cpu().numpy()
                    #sss = sss[0][-3:]
                    #print(sss)
           ii = 0
           if(len(predic) != len(line_list)): print("error")
           for line in line_list:
                line.insert(0,str(class_list[predic[ii]].split(' ')[1]))
                #line.insert(0,str(softmax[ii]))
                #for index in sss:
                #    line.insert(0,str(class_list[index].split(' ')[1]))
                print('\t'.join(line))
                ii += 1
           test_datas = []
           line_list = []
    time_dif = get_time_dif(start_time)
    #print("Time usage:", time_dif)
