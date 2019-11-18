# -*- coding: utf-8 -*-

from urllib import request

nothing = "12345"
for i in range(400):
    f = request.urlopen("http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=" + nothing)
    data = f.read().decode('utf-8')
    nothing = data.split()[-1]
    print(i, data)