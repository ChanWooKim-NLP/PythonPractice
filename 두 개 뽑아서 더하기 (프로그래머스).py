from collections import deque

def solution(numbers):
    answer = []
    numbers = deque(numbers)

    while numbers:
        num = numbers.popleft()

        for value in numbers:
            sum_num = num + value
            answer.append(sum_num)

    answer = sorted(list(set(answer)))
    return answer
