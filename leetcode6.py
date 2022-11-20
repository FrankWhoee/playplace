def convert(s: str, numRows: int) -> str:
    if numRows <= 1:
        return s
    rows = []

    for i in range(numRows):
        rows.append("")

    for i,c in zip(range(len(s)),s):
        if i % (numRows + numRows - 2) < numRows:
            rows[i % (numRows + numRows - 2)] += c
        else:
            rows[numRows - 2 - (i % (numRows + numRows - 2))] += c
    print(rows)
    return "".join(rows)

answer = convert("PAYPALISHIRING", 3)
solution = "PAHNAPLSIIGYIR"
print("Test passed" if answer == solution else "Test failed" + ": " + answer)

answer = convert("PAYPALISHIRING", 4)
solution = "PINALSIGYAHRPI"
print("Test passed" if answer == solution else "Test failed" + ": " + answer)