# -*- coding: utf-8 -*-

s = input()
def decode(s):
    ans = ""
    for c in s:
        if c.isalpha():
            i = ord(c.lower())+2
            if i>ord('z'):
                i -= 26
            c = chr(i)
        ans += c
    return ans

print(decode(s)) # ans = ocr