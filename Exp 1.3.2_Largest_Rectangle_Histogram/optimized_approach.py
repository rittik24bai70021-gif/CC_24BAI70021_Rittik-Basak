def largestRectangleArea(heights):
    stack = []         
    max_area = 0

    heights.append(0)

    for i in range(len(heights)):
        while stack and heights[stack[-1]] > heights[i]:
            height = heights[stack.pop()]

            if stack:
                left = stack[-1]
            else:
                left = -1

    
            width = i - left - 1

            area = height * width
            max_area = max(max_area, area)

        stack.append(i)

    heights.pop()

    return max_area


heights = list(map(int, input("Enter the heights separated by space: ").split()))

print(largestRectangleArea(heights))