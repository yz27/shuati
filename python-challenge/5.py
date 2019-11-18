# -*- coding: utf-8 -*-

from urllib import request
import pickle

url = "http://www.pythonchallenge.com/pc/def/banner.p"
request.urlretrieve(url, filename = 'level5.pkl')
with open("./data/level5.pkl", 'rb') as fp:
    result = pickle.load(fp)

with open("./result/level5_ans.txt", 'w+') as fp:
    for i in result:
        for j in i:
            fp.write(j[0]*j[1])
            print(j[0]*j[1], end='')
        fp.write('\n')
        print('\n')