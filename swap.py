#!/usr/bin/env python3

def swap(a,b):
    x = a
    a = b
    b = x
    return[a,b]

x = input('a = ')
y = input('b = ')
ans = swap(x,y)
print(f"\na = {ans[0]}\nb = {ans[1]}\n")
