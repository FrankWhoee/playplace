slots = 4
access = "C,E,B,C,E,A,D,G,B,C,E,E,E,G,C,G,B,B,D,B"
access = access.split(",")

cache = []
cq = {}

def mincq():
    global cq
    output = cache[0]
    for i in cq.keys():
        if cq[i] < cq[output] and i in cache:
            output = i
    return output
    

hits = 0

for i in access:
    print(cq)
    print(cache)
    print("Evaluating " + i)
    if i not in cache:
        if len(cq) > 0 and len(cache) >= slots:
            evict = mincq()
            print("Cache full. Evicting " + evict)
            cache.remove(evict)
        print(i + " added to cache.")
        if i not in cq:
            cq[i] = 0
        cq[i] += 1
        cache.append(i)
    else:
        print("hit: " + i)
        hits += 1
        cq[i] += 1
    print()
print(cq)
print("total hits: " + str(hits))
print("total misses: " + str(len(access) - hits))
