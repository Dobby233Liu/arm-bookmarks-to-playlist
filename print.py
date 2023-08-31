import json
from itertools import islice

def batched(iterable, n):
    iterator = iter(iterable)
    return iter(
        lambda: tuple(islice(iterator, n)),
        tuple()
    )

def totalclear():
    print("\033c", end="")

startsfrom = "https://m.youtube.com/watch?v=SyX4rgXygwk"
start = 0
day_reqs = 10000/50

with open("dump/-awesome random music-.json","r",encoding="utf-8") as f:
    l = json.load(f)
    if startsfrom:
        start = l.index(startsfrom)
        l = l[l.index(startsfrom):]

totalclear()
print("rest:", len(l))
print("days this could take:", len(l)/day_reqs)
input()

def loop():
    total_now = 0
    last = None
    for i in batched(l, 5):
        totalclear()
        print("\t\t\t\t\t", total_now)
        for j in i:
            print(j)
        last = i[-1]
        total_now += len(i)
        if total_now % (day_reqs/2) == 0:
            rest = total_now/day_reqs
            if rest > 0:
                print("milestone (%d), the rest will take" % (start + total_now), rest, "days")
            else:
                print("done i presume")
        try:
            input()
        except KeyboardInterrupt:
            totalclear()
            print("last was", last)
            return
    totalclear()
loop()