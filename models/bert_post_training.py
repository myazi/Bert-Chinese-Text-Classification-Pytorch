# coding: UTF-8
import torch
import torch.nn as nn
# from pytorch_pretrained_bert import BertModel, BertTokenizer
from pytorch_pretrained import BertModel, BertTokenizer, BertForMaskedLM
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
        self.save_path = dataset + '/saved_dict/post_training_' + self.model_name + '.ckpt'        # 模型训练结果
        self.device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')   # 设备
        self.vocab_size = 21128

        self.require_improvement = 1000                                 # 若超过1000batch效果还没提升，则提前结束训练
        self.num_classes = len(self.class_list)                         # 类别数
        self.num_epochs = 300                                             # epoch数
        self.batch_size = 64                                           # mini-batch大小
        self.pad_size = 16                                              # 每句话处理成的长度(短填长切)
        self.learning_rate = 1e-5                                       # 学习率
        self.bert_path = './bert_pretrain'
        self.tokenizer = BertTokenizer.from_pretrained(self.bert_path)
        self.hidden_size = 768


class Model(nn.Module):

    def __init__(self, config):
        super(Model, self).__init__()
        self.bertformask = BertForMaskedLM.from_pretrained(config.bert_path)
        for param in self.bertformask.parameters():
            param.requires_grad = True

    def forward(self, x):
        context = x[0]  # 输入的句子
        mask = x[2]  # 对padding部分进行mask，和句子一个size，padding部分用0表示，如：[1, 1, 1, 1, 0, 0]
        #print (context.size()) #torch.Size([128, 32])
        prediction_scores = self.bertformask(context, attention_mask=mask)
        return prediction_scores
