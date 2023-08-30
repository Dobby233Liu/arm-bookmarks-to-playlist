import json
from itertools import islice

def batched(iterable, n):
    iterator = iter(iterable)
    return iter(
        lambda: tuple(islice(iterator, n)),
        tuple()
    )

with open("dump/-awesome random music-nonnca-.json","r",encoding="utf-8") as f:
    l= json.load(f)
    for i in batched(l, 5):
        print("\033c", end="")
        for j in i:
            print(j)
        input()
    print("\033c", end="")