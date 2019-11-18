# -*- coding: utf-8 -*-

from collections import Counter
from operator import itemgetter
with open("./data/3.txt", mode='r') as f:
    s = ''.join(f.readlines())

count_dict = Counter(s)

count_dict = sorted(count_dict.items(), key=lambda x: x[1])
print(count_dict)