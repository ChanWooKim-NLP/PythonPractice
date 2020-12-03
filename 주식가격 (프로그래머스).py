from collections import deque


def solution(prices):
    answer = []
    prices = deque(prices)

    while prices:
        price = prices.popleft()
        time = 0

        for i in prices:
            if price > i:
                time += 1
                break
            time += 1
        answer.append(time)

    return answer
