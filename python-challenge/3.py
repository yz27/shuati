# -*- coding: utf-8 -*-

from collections import Counter
from operator import itemgetter
import re
import urllib
with open("./data/3.txt", mode='r') as f:
    s = ''.join(f.readlines())

def search(s):
    result = re.findall("[^A-Z][A-Z]{3}[a-z][A-Z]{3}[^A-Z]", s)
    result = "".join([x[4] for x in result])
    return result

print(search(s))