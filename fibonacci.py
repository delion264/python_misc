#!/usr/bin/python


def fibonacci(a,b,seq,max_len):
    if len(seq) < max_len:
        if a == 0: seq.append(a)
        seq.append(b)
        fibonacci(b,a+b,seq,max_len)
    else:
        return seq

sequence = []
seq_len = 12
fibonacci(0,1,sequence,seq_len)
i = 0
while i < len(sequence):
    print(f"{sequence[i]} ")
    i+=1
