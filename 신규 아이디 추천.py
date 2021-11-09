import re

def solution(new_id:str):
    # 1) 소문자화
    new_id = new_id.lower()

    # 2) 소문자, 숫자, -, _, 마침표 제외 제거
    pattern = re.compile('[^a-z0-9\-_\.]+')
    new_id = re.sub(pattern, '', new_id)

    # 3) 마침표 두 개 이상 하나로 치환
    pattern = re.compile('\.+')
    new_id = re.sub(pattern, '.', new_id)

    # 4) 마침표가 처음/끝에 있을 시 제거
    start_pattern = re.compile('^\.')
    end_pattern = re.compile('\.$')
    new_id = re.sub(start_pattern, '', new_id)
    new_id = re.sub(end_pattern, '', new_id)

    # 5) 빈 문자열에 a 대입
    if len(new_id) == 0:
        new_id = 'a'

    # 6/7) 길이에 따른 조정
    if len(new_id) >= 16:
        new_id = new_id[:15]
        new_id = re.sub(end_pattern, '', new_id)
    elif len(new_id) <= 2:
        new_id += new_id[-1] * (3-len(new_id))

    return new_id
