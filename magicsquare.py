import numpy as np
import itertools

# Brute force magic square solution.
# HOW-TO:
# Flatten your square, and fill in unknowns with -1, then reshape back into square dimensions.
#

square = np.array([19, 89, 84, -1, 74, -1, 49, 59, -1, -1, 69, 39, -1, 29, -1, -1]).reshape(4, 4)
sol = [24, 34, 44, 54, 64, 79, 94]


def verify(input):
    vert = np.sum(input, 0)
    horz = np.sum(input, 1)
    for i in vert:
        if i != vert[0]:
            # print("Failed vertical comparison.")
            return False
    for i in horz:
        if i != vert[0]:
            # print("Failed horizontal comparison.")
            return False
    if np.trace(input) != vert[0]:
        # print("Failed diagonal comparison.")
        return False
    if np.trace(np.fliplr(input)) != vert[0]:
        # print("Failed antidiagonal comparison.")
        return False
    print("All tests passed.")
    return True


permutations = []


def fill(grid,solution):
    j = 0
    output = grid.flatten()
    for i in range(len(output)):
        if output[i] == -1:
            output[i] = solution[j]
            j += 1
    return np.reshape(output,grid.shape)


permutations = list(itertools.permutations(sol))
print(len(permutations))
for i in permutations:
    if verify(fill(square,i)):
        print(i)
        break

