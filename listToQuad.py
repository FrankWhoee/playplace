input = [(27088, 45217, 22916, 1048395), (34557, 18940, 19224, 1048242), (13811, 43502, 60421, 1048034), (2977, 54814, 11119, 1047875), (15468, 12754, 59599, 1047744), (30543, 43852, 14168, 1047685), (42839, 46978, 63607, 1047533), (2189, 40800, 14181, 1047403)]

for t in input:
    for ti in t:
        print(".quad " + hex(ti))
    print('')