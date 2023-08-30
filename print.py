import json
from itertools import islice

def batched(iterable, n):
    iterator = iter(iterable)
    return iter(
        lambda: tuple(islice(iterator, n)),
        tuple()
    )

startsfrom = "https://m.youtube.com/watch?v=sQTZ_qscox0"
with open("dump/-awesome random music-.json","r",encoding="utf-8") as f:
    l= json.load(f)
    if startsfrom:
        l = l[l.index(startsfrom):]
    print(len(l))
    print("days this could take:", len(l)/200)
    input()
    for i in batched(l, 5):
        print("\033c", end="")
        for j in i:
            print(j)
        input()
    print("\033c", end="")