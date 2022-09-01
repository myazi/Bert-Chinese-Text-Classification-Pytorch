cd ./bin
cat ../data/paper_data/clue/thucnews/test.txt | /root/anaconda3/envs/pytorch/bin/python ./run_predict.py --model bert_softmax > ../data/paper_data/clue/thucnews/pre_test.txt
