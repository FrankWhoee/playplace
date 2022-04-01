slots = 4
access = "E,E,A,E,A,E,A,G,A,E,C,B,B,G,B,E,B,E,A,C"
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
    print()
print("total hits: " + str(hits))
