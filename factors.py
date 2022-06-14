#!/usr/bin/python3

import sys

with open(sys.argv[1], "r", encoding="utf-8") as f:
    lines = f.readlines()

    for line in lines:
        n = int(line)
        for i in range(2, n):
            if n % i == 0:
                break;
        print(f"{n}={int(n/i)}*{i}")
