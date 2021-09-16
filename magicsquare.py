import numpy as np
import itertools

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


def permute():
    global permutations
    for a in range(7):
        for b in range(a + 1, a + 6):
            for c in range(b+1, b + 5):
                for d in range(c+1, c + 4):
                    for e in range(d + 1, d + 3):
                        for f in range(e + 1, e + 2):
                            permutations.append([sol[a%7], sol[b%7], sol[c%7], sol[d%7],sol[e%7],sol[f%7],sol[(f+1) % 7]])



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

