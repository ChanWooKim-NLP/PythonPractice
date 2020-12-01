import math

def solution(progresses, speeds):
    answer = []
    stack = []

    day_program = {}

    while progresses:
        func, s = progresses.pop(0), speeds.pop(0)
        left = 100 - func
        day = math.ceil(left / s)

        stack.append(day)

    while stack:
        program = stack.pop(0)
        answer.append(program)
        try:
            max_day = max(program, stack[0])
        except:
            break

        if stack[0] < max_day:
            stack[0] = max_day

    for v in answer:
        if v in day_program:
            day_program[v] += 1

        else: day_program[v] = 1

    answer = list(day_program.values())

    return answer


