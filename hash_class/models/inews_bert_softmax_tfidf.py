# coding: UTF-8
import torch
import torch.nn as nn
import torch.nn.functional as F

class Config(object):

    """配置参数"""
    def __init__(self, dataset):
        self.model_name = 'inews_hash_softmax_onehot'

        self.train_path = dataset + '/hash_data/inews_train_tfidf.txt'                                # 训练集
        self.dev_path = dataset + '/hash_data/inews_dev_tfidf.txt'                                    # 验证集
        self.test_path = dataset + '/hash_data/inews_test_tfidf.txt'                                  # 测试集
        self.class_list = [x.strip() for x in open(
            dataset + '/hash_data/inews_class.txt').readlines()]                                # 类别名单
        self.save_path = dataset + '/saved_dict/' + self.model_name + '.ckpt'        # 模型训练结果
        self.device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')   # 设备

        self.require_improvement = 1000                                 # 若超过1000batch效果还没提升，则提前结束训练
        self.num_classes = len(self.class_list)                         # 类别数
        self.num_epochs = 30                                             # epoch数
        self.batch_size = 128                                           # mini-batch大小
        self.learning_rate = 5e-5                                       # 学习率
        self.hidden_size = 100000


class Model(nn.Module):

    def __init__(self, config):
        super(Model, self).__init__()
        #self.fc = nn.Linear(config.hidden_size, config.num_classes)
        self.fc1 = nn.Linear(config.hidden_size, 384)
        self.fc2 = nn.Linear(384, config.num_classes)

    def forward(self, x):
        #print (pooled.size()) #torch.Size([128, 768])
        out1 = F.relu(self.fc1(x))
        out = F.relu(self.fc2(out1))
        return out
