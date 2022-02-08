#!/usr/bin/python

import random

alphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
special = "!@#$%&*()\'\"-+_=,./:;<>?[]\\^`{\}_~"
pchars = ["integer", "letter", "special"]
pass_len = 32
passwd = ""
i = 0
while i < pass_len:
    ch = random.choice(pchars);
    if ch == "integer":
        passwd = passwd + str(random.randint(0,9))
    elif ch == "letter":
        passwd = passwd + random.choice(alphabet)
    elif ch == "special":
        passwd = passwd + random.choice(special)
    i+=1

print(f"\n{passwd}\n")
print(f"password length = {len(passwd)}\n")
