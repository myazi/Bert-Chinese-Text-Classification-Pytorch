# coding: UTF-8
import torch
from tqdm import tqdm
import time
from datetime import timedelta

PAD, CLS = '[PAD]', '[CLS]'  # padding符号, bert中综合信息符号

def build_dataset_hash(config, rep_type):
    def load_dataset(path):
        contents = []
        with open(path, 'r', encoding='UTF-8') as f:
            i = 0
            for line in tqdm(f):
                lin = line.strip()
                if not lin or len(line.strip().split('\t')) < 2:
                    continue
                if rep_type == "hash" or rep_type == "vec":
                    label,x = lin.split('\t')
                    x = x.strip('\n').split('_')
                    #x = [float(i) for i in x]
                    x = [ 1 if(float(i)>=0)  else -1 for i in x]
                    contents.append((x, int(label)))
                if rep_type == "one-hot":
                    label,x = lin.split('\t')
                    x = x.strip('\n').split('_')
                    x = [int(i) for i in x]
                    index = [i] * len(x)
                    i += 1
                    contents.append((x,index,int(label)))
                if rep_type == "tfidf":
                    label,x = lin.split('\t')
                    x = x.strip('\n').split('_')
                    index = [i] * len(x)
                    i += 1
                    x_col = [int(_.split('|')[0]) for _ in x]
                    x_value = [float(_.split('|')[1]) for _ in x]
                    contents.append((x_col,index,x_value,int(label)))
        return contents
    train = load_dataset(config.train_path)
    dev = load_dataset(config.dev_path)
    test = load_dataset(config.test_path)
    return train, dev, test

def build_dataset_test(config):
    def load_dataset(path, pad_size=32):
        contents = []
        with open(path, 'r', encoding='UTF-8') as f:
            for line in tqdm(f):
                lin = line.strip()
                if not lin:
                    continue
                #label, label_text, id_text, content = lin.split('_!_')
                nid, label,label_text, content1,content2 = lin.split('_!_')
                if int(label) <= 104:
                    label = int(label) - 100
                if int(label) > 105 and int(label) < 111:
                    label = int(label) - 101
                if int(label) > 111:
                    label = int(label) - 102
                content = content1 + content2
                token = config.tokenizer.tokenize(content)
                token = [CLS] + token
                seq_len = len(token)
                mask = []
                token_ids = config.tokenizer.convert_tokens_to_ids(token)

                if pad_size:
                    if len(token) < pad_size:
                        mask = [1] * len(token_ids) + [0] * (pad_size - len(token))
                        token_ids += ([0] * (pad_size - len(token)))
                    else:
                        mask = [1] * pad_size
                        token_ids = token_ids[:pad_size]
                        seq_len = pad_size
                contents.append((token_ids, int(label), seq_len, mask))
        return contents
    train = load_dataset(config.train_path, config.pad_size)
    dev = load_dataset(config.dev_path, config.pad_size)
    test = load_dataset(config.test_path, config.pad_size)
    return train, dev, test

def build_dataset(config):
    def load_dataset(path, pad_size=32):
        contents = []
        with open(path, 'r', encoding='UTF-8') as f:
            for line in tqdm(f):
                lin = line.strip()
                if not lin:
                    continue
                content, label = lin.split('\t')
                token = config.tokenizer.tokenize(content)
                token = [CLS] + token
                seq_len = len(token)
                mask = []
                token_ids = config.tokenizer.convert_tokens_to_ids(token)

                if pad_size:
                    if len(token) < pad_size:
                        mask = [1] * len(token_ids) + [0] * (pad_size - len(token))
                        token_ids += ([0] * (pad_size - len(token)))
                    else:
                        mask = [1] * pad_size
                        token_ids = token_ids[:pad_size]
                        seq_len = pad_size
                contents.append((token_ids, int(label), seq_len, mask))
        return contents
    train = load_dataset(config.train_path, config.pad_size)
    dev = load_dataset(config.dev_path, config.pad_size)
    test = load_dataset(config.test_path, config.pad_size)
    return train, dev, test


def build_dataset_withtag(config):
    def load_dataset(path, pad_size=32):
        contents = []
        with open(path, 'r', encoding='UTF-8') as f:
            for line in tqdm(f):
                lin = line.strip('\n')
                if not lin:
                    continue
                content, tag, label = lin.split('\t')
                token = config.tokenizer.tokenize(content)
                token = [CLS] + token
                seq_len = len(token)
                mask = []
                token_ids = config.tokenizer.convert_tokens_to_ids(token)
                if pad_size:
                    if len(token) < pad_size:
                        mask = [1] * len(token_ids) + [0] * (pad_size - len(token))
                        token_ids += ([0] * (pad_size - len(token)))
                    else:
                        mask = [1] * pad_size
                        token_ids = token_ids[:pad_size]
                        seq_len = pad_size
                
                token = config.tokenizer.tokenize(tag)
                token = [CLS] + token
                seq_len_tag = len(token)
                mask_tag = []
                token_ids_tag = config.tokenizer.convert_tokens_to_ids(token)
                if pad_size:
                    if len(token) < pad_size:
                        mask_tag = [1] * len(token_ids_tag) + [0] * (pad_size - len(token))
                        token_ids_tag += ([0] * (pad_size - len(token)))
                    else:
                        mask_tag = [1] * pad_size
                        token_ids_tag = token_ids_tag[:pad_size]
                        seq_len_tag = pad_size
                contents.append((token_ids, int(label), seq_len, mask, token_ids_tag, seq_len_tag, mask_tag))
            return contents
    train = load_dataset(config.train_path, config.pad_size)
    dev = load_dataset(config.dev_path, config.pad_size)
    test = load_dataset(config.test_path, config.pad_size)
    return train, dev, test



def build_dataset_line(config, line):
    contents = []
    lin = line.strip()
    content,label = lin.split('\t')
    token = config.tokenizer.tokenize(content)
    token = [CLS] + token
    seq_len = len(token)
    mask = []
    token_ids = config.tokenizer.convert_tokens_to_ids(token)
    pad_size=32
    if pad_size:
        if len(token) < pad_size:
            mask = [1] * len(token_ids) + [0] * (pad_size - len(token))
            token_ids += ([0] * (pad_size - len(token)))
        else:
            mask = [1] * pad_size
            token_ids = token_ids[:pad_size]
            seq_len = pad_size
    contents.append((token_ids, int(label), seq_len, mask))
    #[([101, 3309, 2521, 2769, 812, 6878, 6224, 3198, 872, 3633, 1962, 3946, 3382, 2769, 1157, 1962, 2768, 4225, 3297, 5401, 704, 2466, 6163, 934, 6163, 934, 6392, 6369, 2157, 1072, 3255, 5543], 0, 32, [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1])]
    #print (contents)
    return contents


def build_dataset_line_withtag(config, line):
    contents = []
    lin = line.strip('\n').split('\t')
    content, tag, label = lin
    token = config.tokenizer.tokenize(content)
    token = [CLS] + token
    seq_len = len(token)
    mask = []
    token_ids = config.tokenizer.convert_tokens_to_ids(token)
    pad_size=32
    if pad_size:
        if len(token) < pad_size:
            mask = [1] * len(token_ids) + [0] * (pad_size - len(token))
            token_ids += ([0] * (pad_size - len(token)))
        else:
            mask = [1] * pad_size
            token_ids = token_ids[:pad_size]
            seq_len = pad_size
                
    token = config.tokenizer.tokenize(tag)
    token = [CLS] + token
    seq_len_tag = len(token)
    mask_tag = []
    token_ids_tag = config.tokenizer.convert_tokens_to_ids(token)
    if pad_size:
        if len(token) < pad_size:
            mask_tag = [1] * len(token_ids_tag) + [0] * (pad_size - len(token))
            token_ids_tag += ([0] * (pad_size - len(token)))
        else:
            mask_tag = [1] * pad_size
            token_ids_tag = token_ids_tag[:pad_size]
            seq_len_tag = pad_size
    contents.append((token_ids, int(label), seq_len, mask, token_ids_tag, seq_len_tag, mask_tag))
    #contents.append((token_ids, int(label), seq_len, mask))
    #[([101, 3309, 2521, 2769, 812, 6878, 6224, 3198, 872, 3633, 1962, 3946, 3382, 2769, 1157, 1962, 2768, 4225, 3297, 5401, 704, 2466, 6163, 934, 6163, 934, 6392, 6369, 2157, 1072, 3255, 5543], 0, 32, [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1])]
    #print (contents)
    return contents

class DatasetIterater(object):
    def __init__(self, batches, batch_size, device):
        self.batch_size = batch_size
        self.batches = batches
        self.n_batches = len(batches) // batch_size
        self.residue = False  # 记录batch数量是否为整数
        if len(batches) % self.n_batches != 0:
            self.residue = True
        self.index = 0
        self.device = device

    def _to_tensor(self, datas):
        x = torch.LongTensor([_[0] for _ in datas]).to(self.device)
        y = torch.LongTensor([_[1] for _ in datas]).to(self.device)

        # pad前的长度(超过pad_size的设为pad_size)
        seq_len = torch.LongTensor([_[2] for _ in datas]).to(self.device)
        mask = torch.LongTensor([_[3] for _ in datas]).to(self.device)
        return (x, seq_len, mask), y

        #x_tag = torch.LongTensor([_[4] for _ in datas]).to(self.device)
        #seq_len_tag = torch.LongTensor([_[5] for _ in datas]).to(self.device)
        #mask_tag = torch.LongTensor([_[6] for _ in datas]).to(self.device)
        #return (x, seq_len, mask, x_tag, seq_len_tag, mask_tag), y
         


    def __next__(self):
        if self.residue and self.index == self.n_batches:
            batches = self.batches[self.index * self.batch_size: len(self.batches)]
            self.index += 1
            batches = self._to_tensor(batches)
            return batches

        elif self.index >= self.n_batches:
            self.index = 0
            raise StopIteration
        else:
            batches = self.batches[self.index * self.batch_size: (self.index + 1) * self.batch_size]
            self.index += 1
            batches = self._to_tensor(batches)
            return batches

    def __iter__(self):
        return self

    def __len__(self):
        if self.residue:
            return self.n_batches + 1
        else:
            return self.n_batches

class DatasetIterater_hash(object):
    def __init__(self, batches, batch_size, device, rep_type):
        self.batch_size = batch_size
        self.batches = batches
        self.n_batches = len(batches) // batch_size
        self.residue = False  # 记录batch数量是否为整数
        if len(batches) % self.n_batches != 0:
            self.residue = True
        self.index = 0
        self.device = device
        self.rep_type = rep_type

    def _to_tensor(self, datas,batch_size, rep_type):
        if rep_type == "tfidf":
            icol = [int(icol) for _ in datas for icol in _[0]]
            print(icol)
            irow = [int(irow%batch_size) for _ in datas for irow in _[1]]
            print(irow)
            value = [float(value) for _ in datas for value in _[2]]
            print(value)
            fact_batch_size = max(irow) + 1
            x = torch.sparse.FloatTensor(torch.LongTensor([irow,icol]), torch.FloatTensor(value), torch.Size((fact_batch_size,100000))).to_dense().to(self.device)
            y = torch.LongTensor([_[3] for _ in datas]).to(self.device)
        if rep_type == "one-hot":
            icol = [int(icol) for _ in datas for icol in _[0]]
            print(icol)
            irow = [int(irow%batch_size) for _ in datas for irow in _[1]]
            print(irow)
            fact_batch_size = max(irow) + 1
            x = torch.sparse.FloatTensor(torch.LongTensor([irow,icol]), torch.FloatTensor([1] * len(irow)), torch.Size((fact_batch_size,100000))).to_dense().to(self.device)
            y = torch.LongTensor([_[2] for _ in datas]).to(self.device)
        if rep_type == "hash" or rep_type =="vec":
            x = torch.Tensor([_[0] for _ in datas]).to(self.device)
            #x.requires_grad = True
            y = torch.LongTensor([_[1] for _ in datas]).to(self.device)

        return x, y

    def __next__(self):
        if self.residue and self.index == self.n_batches:
            batches = self.batches[self.index * self.batch_size: len(self.batches)]
            batch_size = self.batch_size
            rep_type = self.rep_type
            self.index += 1
            batches = self._to_tensor(batches, batch_size, rep_type)
            return batches

        elif self.index >= self.n_batches:
            self.index = 0
            raise StopIteration
        else:
            batches = self.batches[self.index * self.batch_size: (self.index + 1) * self.batch_size]
            batch_size = self.batch_size
            rep_type = self.rep_type
            self.index += 1
            batches = self._to_tensor(batches, batch_size, rep_type)
            return batches

    def __iter__(self):
        return self

    def __len__(self):
        if self.residue:
            return self.n_batches + 1
        else:
            return self.n_batches

def build_iterator_hash(dataset, config, rep_type):
    iter = DatasetIterater_hash(dataset, config.batch_size, config.device,rep_type)
    return iter


def build_iterator(dataset, config):
    iter = DatasetIterater(dataset, config.batch_size, config.device)
    return iter

def build_iterator_1(dataset,config):
    iter = DatasetIterater(dataset, 1, config.device)
    #print (iter)
    return iter

def build_iterator_n(dataset, size, config):
    iter = DatasetIterater(dataset, size, config.device)
    #print (iter)
    return iter

def get_time_dif(start_time):
    """获取已使用时间"""
    end_time = time.time()
    time_dif = end_time - start_time
    return timedelta(seconds=int(round(time_dif)))
