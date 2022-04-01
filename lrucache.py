slots = 4
access = "A,B,A,B,G,B,B,A,A,D,A,E,A,C,E,G,D,B,G,E"
access = access.split(",")

cache = []
cq = []

hits = 0

for i in access:
    print(cq)
    print("Evaluating " + i)
    if i not in cache:
        if len(cq) > 0 and len(cache) >= slots:
            evict = cq.pop(0)
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
