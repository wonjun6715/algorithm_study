# 병합 정렬 알고리즘 혼자 짜보기

from typing import MutableSequence

def merge_sort(a: MutableSequence) -> None:
    """병합 정렬"""
    
    def _merge_sort(a: MutableSequence, left: int, right: int) -> None:
        """a[left] ~ a[right]를 재귀적으로 병합 정렬"""
        if left < right:
            center = (left + right) // 2
            
            _merge_sort(a, left, center)
            _merge_sort(a, center + 1, right)
            
            p = j = 0
            i = k = left
            
            while i <= center:
                buff[p] = a[i]
                p += 1
                i += 1
            
            while j < p and i <= right:
                if buff[j] <= a[i]:
                    a[k] = buff[j]
                    j += 1
                else:
                    a[k] = a[i]
                    i += 1
                k += 1
            
            while j < p:
                a[k] = buff[j]
                k += 1
                j += 1

    n = len(a)
    buff = [None] * n
    merge_sort(a, 0, n - 1) # 배열 전체를 병합 정렬
    del buff