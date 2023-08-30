import json
from itertools import islice

def batched(iterable, n):
    iterator = iter(iterable)
    return iter(
        lambda: tuple(islice(iterator, n)),
        tuple()
    )

startsfrom = "https://m.youtube.com/watch?v=sQTZ_qscox0"
day_reqs = 10000/50

with open("dump/-awesome random music-.json","r",encoding="utf-8") as f:
    l= json.load(f)
    if startsfrom:
        l = l[l.index(startsfrom):]
    print(len(l))
    print("days this could take:", len(l)/day_reqs)
    input()
    total_now = 0
    for i in batched(l, 5):
        print("\033c", end="")
        for j in i:
            print(j)
        total_now += len(i)
        if total_now % day_reqs == 0:
            rest = total_now/day_reqs
            if rest > 0:
                print("milestone, the rest will take", rest, "days")
            else:
                print("done i presume")
        input()
    print("\033c", end="")