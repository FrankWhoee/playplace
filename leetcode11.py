def maxArea(height: list) -> int:
    left = 0
    right = 0
    area = 0
    biggest = left
    while right < len(height):
        if height[right] > height[biggest]:
            left = biggest
        area = max(area, (right - left) * min(height[left], height[right]))
        right += 1
    return area

answer = maxArea([1,8,6,2,5,4,8,3,7])
solution = 49
print("Test passed" if answer == solution else "Test failed" + ": " + str(answer))