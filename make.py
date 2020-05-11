"""产生需要的停用词"""
from itertools import chain

with open('stopwords/use.txt', 'w', encoding='utf-8') as f:
    with open('stopwords/cn_stopwords.txt', encoding='utf-8') as cn,\
        open('stopwords/hit_stopwords.txt', encoding='utf-8') as hit,\
        open('stopwords/scu_stopwords.txt', encoding='utf-8') as scu,\
        open('stopwords/baidu_stopwords.txt', encoding='utf-8') as baidu:
        for word in chain(cn, hit, scu, baidu):
            f.write(word)


