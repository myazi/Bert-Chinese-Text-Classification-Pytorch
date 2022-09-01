### bert 实验

#/root/anaconda3/envs/pytorch/bin/python run.py --model bert_softmax  > ./log/bert_softmax
#/root/anaconda3/envs/pytorch/bin/python run.py --model bert_softmax_thucnews  > ../log/bert_softmax_thucnews
#/root/anaconda3/envs/pytorch/bin/python run.py --model bert_softmax_inews  > ../log/bert_softmax_inews

### hash 实验运行前1）对应model下的模型加载相应的数据，2）在Keyword中注意数据格式产出样本数据，3）不同样本数据主要util里面解释不同(x,label)，4）model下面网络参数与特征长度一致

########## toutiao dataset
cd ./hash_class

## hash
#/root/anaconda3/envs/pytorch/bin/python hash_class.py ../data/paper_data/clue/tnews/toutiao_category_test.txt  hash tnews > ../data/hash_data/toutiao_category_test_hash.txt
#/root/anaconda3/envs/pytorch/bin/python hash_class.py ../data/paper_data/clue/tnews/toutiao_category_train.txt hash tnews > ../data/hash_data/toutiao_category_train_hash.txt
#/root/anaconda3/envs/pytorch/bin/python hash_class.py ../data/paper_data/clue/tnews/toutiao_category_dev.txt  hash tnews > ../data/hash_data/toutiao_category_dev_hash.txt
#/root/anaconda3/envs/pytorch/bin/python run.py --model toutiao_bert_softmax_hash --rep_type hash > ../log/toutiao_bert_softmax_hash

## word2vec
#/root/anaconda3/envs/pytorch/bin/python hash_class.py ../data/paper_data/clue/tnews/toutiao_category_test.txt  word2vec tnews > ../data/hash_data/toutiao_category_test_vec.txt
#/root/anaconda3/envs/pytorch/bin/python hash_class.py ../data/paper_data/clue/tnews/toutiao_category_train.txt word2vec tnews > ../data/hash_data/toutiao_category_train_vec.txt
#/root/anaconda3/envs/pytorch/bin/python hash_class.py ../data/paper_data/clue/tnews/toutiao_category_dev.txt  word2vec tnews > ../data/hash_data/toutiao_category_dev_vec.txt
#/root/anaconda3/envs/pytorch/bin/python run.py --model toutiao_bert_softmax_vec --rep_type vec > ../log/toutiao_bert_softmax_vec

## one-hot
#/root/anaconda3/envs/pytorch/bin/python hash_class.py ../data/paper_data/clue/tnews/toutiao_category_test.txt  onehot tnews > ../data/hash_data/toutiao_category_test_onehot.txt
#/root/anaconda3/envs/pytorch/bin/python hash_class.py ../data/paper_data/clue/tnews/toutiao_category_train.txt onehot tnews > ../data/hash_data/toutiao_category_train_onehot.txt
#/root/anaconda3/envs/pytorch/bin/python hash_class.py ../data/paper_data/clue/tnews/toutiao_category_dev.txt  onehot tnews > ../data/hash_data/toutiao_category_dev_onehot.txt
#/root/anaconda3/envs/pytorch/bin/python run.py --model toutiao_bert_softmax_onehot --rep_type one-hot > ../log/toutiao_bert_softmax_onehot

## tfidf
#/root/anaconda3/envs/pytorch/bin/python hash_class.py ../data/paper_data/clue/tnews/toutiao_category_all.txt  tfidf tnews > ../data/hash_data/toutiao_category_all_tfidf.txt
#/root/anaconda3/envs/pytorch/bin/python run.py --model toutiao_bert_softmax_tfidf --rep_type tfidf > ../log/toutiao_bert_softmax_tfidf

########## thucnews dataset

## hash
#/root/anaconda3/envs/pytorch/bin/python hash_class.py ../data/paper_data/clue/thucnews/test.txt  hash thucnews > ../data/hash_data/thucnews_test_hash.txt
#/root/anaconda3/envs/pytorch/bin/python hash_class.py ../data/paper_data/clue/thucnews/train.txt hash thucnews > ../data/hash_data/thucnews_train_hash.txt
#/root/anaconda3/envs/pytorch/bin/python hash_class.py ../data/paper_data/clue/thucnews/dev.txt  hash thucnews > ../data/hash_data/thucnews_dev_hash.txt
/root/anaconda3/envs/pytorch/bin/python  run.py --model thucnews_bert_softmax_hash --rep_type hash > ../log/thucnews_bert_softmax_hash

## word2vec
#/root/anaconda3/envs/pytorch/bin/python hash_class.py ../data/paper_data/clue/thucnews/test.txt  word2vec thucnews > ../data/hash_data/thucnews_test_vec.txt
#/root/anaconda3/envs/pytorch/bin/python hash_class.py ../data/paper_data/clue/thucnews/train.txt word2vec thucnews > ../data/hash_data/thucnews_train_vec.txt
#/root/anaconda3/envs/pytorch/bin/python hash_class.py ../data/paper_data/clue/thucnews/dev.txt  word2vec thucnews > ../data/hash_data/thucnews_dev_vec.txt
#/root/anaconda3/envs/pytorch/bin/python run.py --model thucnews_bert_softmax_vec --rep_type vec > ../log/thucnews_bert_softmax_vec

## one-hot
#/root/anaconda3/envs/pytorch/bin/python hash_class.py ../data/paper_data/clue/thucnews/test.txt  onehot thucnews > ../data/hash_data/thucnews_test_onehot.txt
#/root/anaconda3/envs/pytorch/bin/python hash_class.py ../data/paper_data/clue/thucnews/train.txt onehot thucnews > ../data/hash_data/thucnews_train_onehot.txt
#/root/anaconda3/envs/pytorch/bin/python hash_class.py ../data/paper_data/clue/thucnews/dev.txt  onehot thucnews > ../data/hash_data/thucnews_dev_onehot.txt
#/root/anaconda3/envs/pytorch/bin/python run.py --model thucnews_bert_softmax_onehot --rep_type one-hot > ../log/thucnews_bert_softmax_onehot

## tfidf
#/root/anaconda3/envs/pytorch/bin/python hash_class.py ../data/paper_data/clue/thucnews/all.txt tfidf thucnews > ../data/hash_data/thucnews_all_tfidf.txt
#/root/anaconda3/envs/pytorch/bin/python run.py --model thucnews_bert_softmax_tfidf --rep_type tfidf > ../log/thucnews_bert_softmax_tfidf

########## inews dataset

## hash
#/root/anaconda3/envs/pytorch/bin/python hash_class.py ../data/paper_data/clue/inews/test.txt  hash inews > ../data/hash_data/inews_test_hash.txt
#/root/anaconda3/envs/pytorch/bin/python hash_class.py ../data/paper_data/clue/inews/train.txt hash inews > ../data/hash_data/inews_train_hash.txt
#/root/anaconda3/envs/pytorch/bin/python hash_class.py ../data/paper_data/clue/inews/dev.txt  hash inews > ../data/hash_data/inews_dev_hash.txt
#/root/anaconda3/envs/pytorch/bin/python run.py --model inews_bert_softmax_hash --rep_type hash > ../log/inews_bert_softmax_hash

## word2vec
#/root/anaconda3/envs/pytorch/bin/python hash_class.py ../data/paper_data/clue/inews/test.txt  word2vec inews > ../data/hash_data/inews_test_vec.txt
#/root/anaconda3/envs/pytorch/bin/python hash_class.py ../data/paper_data/clue/inews/train.txt word2vec inews > ../data/hash_data/inews_train_vec.txt
#/root/anaconda3/envs/pytorch/bin/python hash_class.py ../data/paper_data/clue/inews/dev.txt  word2vec inews > ../data/hash_data/inews_dev_vec.txt
#/root/anaconda3/envs/pytorch/bin/python run.py --model inews_bert_softmax_vec --rep_type vec > ../log/inews_bert_softmax_vec

## one-hot
#/root/anaconda3/envs/pytorch/bin/python hash_class.py ../data/paper_data/clue/inews/test.txt onehot inews > ../data/hash_data/inews_test_onehot.txt
#/root/anaconda3/envs/pytorch/bin/python hash_class.py ../data/paper_data/clue/inews/train.txt onehot inews > ../data/hash_data/inews_train_onehot.txt
#/root/anaconda3/envs/pytorch/bin/python hash_class.py ../data/paper_data/clue/inews/dev.txt onehot inews > ../data/hash_data/inews_dev_onehot.txt
#/root/anaconda3/envs/pytorch/bin/python run.py --model inews_bert_softmax_onehot --rep_type one-hot > ../log/inews_bert_softmax_onehot

## tfidf
#/root/anaconda3/envs/pytorch/bin/python hash_class.py ../data/paper_data/clue/inews/all.txt tfidf inews > ../data/hash_data/inews_all_tfidf.txt
#/root/anaconda3/envs/pytorch/bin/python run.py --model inews_bert_softmax_tfidf --rep_type tfidf > ../log/inews_bert_softmax_tfidf
