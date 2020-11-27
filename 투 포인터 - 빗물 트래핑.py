# 투 포인터 이용

def solution1(height):
    if not height:
        return 0

    volume = 0
    left, right = 0, len(height) - 1
    left_max, right_max = height[left], height[right] # 현재 위치
    
    # 높은 쪽을 향해서 포인터가 이동함. 민약 왼쪽이 높으면 오른쪽에서 하나 깎음
    while left < right: # 포인터가 역전되면 안됨
        left_max, right_max = max(height[left], left_max),\     # 갱신된 현재 왼쪽 / 오른쪽 위치와 기존 위치 간  
                                max(height[right], right_max)

        if left_max <= right_max:
            volume += left_max - height[left]
            left += 1

        else:
            volume += right_max - height[right]
            right -= 1

    return volume


