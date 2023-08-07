# coding: UTF-8
import time
import torch
import torch.nn as nn
import numpy as np
from train_eval import train, init_network
from importlib import import_module
import argparse


from utils import build_dataset, build_dataset_test,build_dataset_hash, build_dataset_withtag, build_iterator, build_iterator_hash,get_time_dif
#from utils import build_dataset, build_iterator, get_time_dif
import os

os.environ["CUDA_VISIBLE_DEVICES"] = "0"
parser = argparse.ArgumentParser(description='Chinese Text Classification')
parser.add_argument('--model', type=str, required=True, help='choose a model: Bert, ERNIE')
parser.add_argument('--rep_type', type=str, required=True, help='choose a rep_type: one-hot,tfidf,hash,vec')
args = parser.parse_args()


if __name__ == '__main__':
    #dataset = 'THUCNews'  # 数据集
    dataset = '../data'
    model_name = args.model  # bert
    rep_type = args.rep_type
    x = import_module('models.' + model_name)
    config = x.Config(dataset)
    np.random.seed(1)
    torch.manual_seed(1)
    torch.cuda.manual_seed_all(1)
    torch.backends.cudnn.deterministic = True  # 保证每次结果一样

    start_time = time.time()
    print("Loading data...")
    #train_data, dev_data, test_data = build_dataset(config)
    train_data, dev_data, test_data = build_dataset_hash(config, rep_type)
    train_iter = build_iterator_hash(train_data, config, rep_type)
    dev_iter = build_iterator_hash(dev_data, config, rep_type)
    test_iter = build_iterator_hash(test_data, config, rep_type)
    time_dif = get_time_dif(start_time)
    print("Time usage:", time_dif)

    # train
    model = x.Model(config).to(config.device)
    model = nn.DataParallel(model) #多gpu训练
    train(config, model, train_iter, dev_iter, test_iter)
