slots = 4
access = "D,A,A,E,B,G,E,E,E,B,D,G,C,D,A,G,A,G,D,C"
access = access.split(",")

cache = []
cq = []

hits = 0

for i in access:
    print(cq)
    print("Evaluating " + i)
    if i not in cache:
        if len(cq) > 0 and len(cache) >= slots:
            evict = cq.pop()
            print("Cache full. Evicting " + evict)
            cache.remove(evict)
        print(i + " added to cache.")
        cq.append(i)
        cache.append(i)
    else:
        print("hit: " + i)
        hits += 1
        cq.remove(i)
        cq.append(i)
    print()
print("total hits: " + str(hits))
