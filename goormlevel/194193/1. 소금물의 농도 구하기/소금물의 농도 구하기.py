# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean

from math import floor

n, m = map(int, input().split())

salt = n * 0.07

answer = str((salt / (n+m)) * 100)

a, b = answer.split('.')
print(a + '.' + b[:2])