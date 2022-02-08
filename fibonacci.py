#!/usr/bin/python


def fibonacci(a,b,seq,max_len):
    if len(seq) < max_len:
        if a == 0: seq.append(a)
        seq.append(b)
        fibonacci(b,a+b,seq,max_len)
    else:
        return seq

sequence = []
seq_len = int(input("How many fibonacci numbers do you want to see? "))
fibonacci(0,1,sequence,seq_len)
print(sequence)
