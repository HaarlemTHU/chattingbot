import argparse


# 对话模型超参数
def generate_hparams():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '--max_samples',
        default=450000,
        type=int,
        help='maximum number of conversation pairs to use')
    parser.add_argument('--batch_size', default=128, type=int)
    parser.add_argument('--vocab_size', default=20000, type=int)
    parser.add_argument('--embedding_dim', default=128, type=int)
    parser.add_argument('--units', default=256, type=int)
    parser.add_argument('--enc_vocab_size', default=20000, type=int)
    parser.add_argument('--dec_vocab_size', default=20000, type=int)
    parser.add_argument('--epoch', default=40, type=int)
    # 使用了绝对路径，需要修改
    parser.add_argument('--ckpt_dir', default='C:\\Users\\MI\\Desktop\\人工智能实践\\chattingbot\\model', type=str,
                        help='model save path')
    # 使用了绝对路径，需要修改
    parser.add_argument('--data_path', default='C:\\Users\\MI\\Desktop\\人工智能实践\\chattingbot\\code\\xhj.csv',
                        type=str, help='data save path')

    hparams = parser.parse_args()
    return hparams


