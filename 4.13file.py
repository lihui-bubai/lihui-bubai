import argparse

parser = argparse.ArgumentParser()

parser.add_argument('--lr', default=0.001, help='learning rate', type=float)
parser.add_argument('--batch_size', default=2048, help='batch size', type=int)
parser.add_argument('--test_batch_size', default= 1, help='batch size', type=int)
parser.add_argument('--number_sample', default= 1000, help='negative sampling number', type=int)
parser.add_argument('--top_folder', default="/home/chao/haoyu/dien-taobao/", help='top folder') #"/home/chao/haoyu/dien-nsma/" #"/cluster/home/it_stu110/rec/dien-nsma" 
parser.add_argument('--model_type', default="DIN", help='model name')
parser.add_argument('--seed', default= 3, help='seed', type=int)
parser.add_argument('--train_rounds', default= 4, help='seed', type=int)
parser.add_argument('--embed_size', default= 18, help='embed size', type=int)
parser.add_argument('--test_iter', default= 50, help='test iterations', type=int)
parser.add_argument('--save_iter', default= 50, help='save iterations', type=int)
parser.add_argument('--should_train', action='store_true', help='train model')
parser.add_argument('--should_test', action='store_true', help='eval model')

parser.add_argument('--dataset', default="taobao", help='dataset')

args = parser.parse_args()
