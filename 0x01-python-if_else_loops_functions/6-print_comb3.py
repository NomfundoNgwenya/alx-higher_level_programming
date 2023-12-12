#!/usr/bin/python3
for t in range(10):
    for u in range(t + 1, 10):
        print("{:d}{:d}".format(t, u), end=", " if (t, u) != (8, 9) else "\n")
