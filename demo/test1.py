# -*- coding: utf-8 -*-
print("你好")
import sys
def test():
    args=sys.argv
    if len(args)==1:
        print("hello world!")
    elif len(args)==2:
        print("hello,%s!" %args[1])
    else:
        print("Too many args!")
if __name__=="__main__":
    test()