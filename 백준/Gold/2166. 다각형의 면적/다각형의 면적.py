n = int(input())

points = []
for _ in range(n):
    x, y = map(int, input().split())
    points.append((x, y))

points.append(points[0])

# ccw 알고리즘 응용
x, y = 0, 0
for i in range(n):
    x += points[i][0] * points[i+1][1]
    y += points[i][1] * points[i+1][0]

answer = abs(round((x-y)/2, 1))
print(answer)