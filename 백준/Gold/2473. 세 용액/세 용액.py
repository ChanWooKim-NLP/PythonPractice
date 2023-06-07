n = int(input())

arr = list(map(int, input().split()))

arr.sort()

def find_closest_sum():
    close_sum = float('inf')
    closest_combination = [0, 0, 0]
    
    for i in range(n-2):
        left, mid, right = i, i+1, n-1
        
        while mid < right:
            sum_val = arr[left] + arr[mid] + arr[right]
            
            if abs(sum_val) < abs(close_sum):
                close_sum = sum_val
                closest_combination = [arr[left], arr[mid], arr[right]]
                
            if sum_val < 0:
                mid += 1
                
            else:
                right -= 1
                
    return closest_combination

result = find_closest_sum()
print(*result)