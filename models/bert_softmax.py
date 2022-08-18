# coding: UTF-8
import torch
import torch.nn as nn
# from pytorch_pretrained_bert import BertModel, BertTokenizer
from pytorch_pretrained import BertModel, BertTokenizer
import torch.nn.functional as F

class Config(object):

    """配置参数"""
    def __init__(self, dataset):
        self.model_name = 'bert_softmax'
        #self.train_path = dataset + '/paper_data/clue/thucnews/train.txt'                                # 训练集
        #self.dev_path = dataset + '/paper_data/clue/thucnews/dev.txt'                                    # 验证集
        #self.test_path = dataset + '/paper_data/clue/thucnews/test.txt'                                  # 测试集
        #self.class_list = [x.strip() for x in open(
        #    dataset + '/paper_data/clue/thucnews/thucnews_class.txt').readlines()]                                # 类别名单

        #self.train_path = dataset + '/paper_data/clue/inews/train.txt'                                # 训练集
        #self.dev_path = dataset + '/paper_data/clue/inews/dev.txt'                                    # 验证集
        #self.test_path = dataset + '/paper_data/clue/inews/test.txt'                                  # 测试集
        #self.class_list = [x.strip() for x in open(
        #    dataset + '/paper_data/clue/inews/inews_class.txt').readlines()]                                # 类别名单

        self.train_path = dataset + '/paper_data/clue/tnews/toutiao_category_train.txt'                                # 训练集
        self.dev_path = dataset + '/paper_data/clue/tnews/toutiao_category_dev.txt'                                    # 验证集
        self.test_path = dataset + '/paper_data/clue/tnews/toutiao_category_test.txt'                                  # 测试集
        self.class_list = [x.strip() for x in open(
            dataset + '/paper_data/clue/tnews/class.txt').readlines()]                                # 类别名单
        self.save_path = dataset + '/saved_dict/' + self.model_name + '.ckpt'        # 模型训练结果
        self.device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')   # 设备
        print(self.device)

        self.require_improvement = 1000                                 # 若超过1000batch效果还没提升，则提前结束训练
        self.num_classes = len(self.class_list)                         # 类别数
        self.num_epochs = 3                                             # epoch数
        self.batch_size = 128                                           # mini-batch大小
        self.pad_size = 32                                              # 每句话处理成的长度(短填长切)
        self.learning_rate = 5e-5                                       # 学习率
        self.bert_path = './bert_pretrain'
        self.tokenizer = BertTokenizer.from_pretrained(self.bert_path)
        self.hidden_size = 768


class Model(nn.Module):

    def __init__(self, config):
        super(Model, self).__init__()
        self.bert = BertModel.from_pretrained(config.bert_path)
        for param in self.bert.parameters():
            param.requires_grad = True
        #self.fc = nn.Linear(config.hidden_size, config.num_classes)
        self.fc1 = nn.Linear(config.hidden_size, 384)
        self.fc2 = nn.Linear(384, config.num_classes)

    def forward(self, x):
        context = x[0]  # 输入的句子
        mask = x[2]  # 对padding部分进行mask，和句子一个size，padding部分用0表示，如：[1, 1, 1, 1, 0, 0]
        #print (context.size()) #torch.Size([128, 32])
        _, pooled = self.bert(context, attention_mask=mask, output_all_encoded_layers=False)
        #print (pooled.size()) #torch.Size([128, 768])
        out1 = F.relu(self.fc1(pooled))
        out = F.relu(self.fc2(out1))
        return out
