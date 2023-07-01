# 버블 정렬 알고리즘 구현하기(알고리즘의 개선1: 정렬을 모두 마쳤거나 정렬이 거의 다 된 배열의 경우 중단 방식 적용)

from typing import MutableSequence

def bubble_sort(a: MutableSequence) -> None:
    """버블 정렬(교환 횟수에 따른 중단)"""
    n = len(a)
    for i in range(n - 1):
        exchng = 0
        for j in range(n - 1, i, -1):
            if a[j - 1] > a[j]:
                a[j - 1], a[j] = a[j], a[j - 1]
                exchng += 1
            if exchng == 0:
                break

