# 오픈 주소법으로 해시 함수 구현하기

from __future__ import annotations
from typing import Sequence, Any
from enum import Enum
import hashlib

# 버킷의 속성
class Status(Enum):
    OCCUPIED = 0 # 데이터를 저장
    EMPTY = 1 # 비어 있음
    DELETED = 2 # 삭제 완료
    
class Bucket:
    """해시를 구성하는 버킷"""
    
    def __init__(self, key: Any = None, value: Any = None, stat: Status = Status.EMPTY) -> None:
        """초기화"""
        self.key = key # 키 
        self.value = value # 값
        self.stat = stat # 속성
        
    def set(self, key: Any, value: Any, stat: Status) -> None:
        """모든 필드에 값을 설정"""
        self.key = key # 키
        self.value = value # 값 
        self.stat = stat # 속성
        
    def set_status(self, stat: Status) -> None:
        """속성을 설정"""
        self.stat = stat

class OpenHash:
    """오픈 주소법으로 구현하는 해시 클래스"""
    
    def __init___(self, capacity: int) -> None:
        """초기화"""
        self.capacity = capacity  # 해시 테이블의 크기를 지정
        self.table = [Bucket()] * self.capacity #  해시 테이블
    
    def hash_value(self, key: Any) -> int:
        """해시값을 구함"""
        if isinstance(key, int):
            return key % self.capacity
        return(int(hashlib.md5(str(key).encode()).hexdigest(), 16) % self.capacity)
    
    def rehash_value(self, key: Any) -> int:
        """재해시값을 구함"""
        return(self.hash_value(key) + 1) % self.capacity 
        """self.capacity 나머지 연산을 한번 더 해주는 이유는 만약 기존의 해시값이 마지막 버킷을 가리키고 있다면
        나머지 연산을 통해 다시 첫번째 버킷을 가리키게 하기 위함"""
    
    def search_node(self, key: Any) -> Any:
        """키가 key인 버킷을 검색"""
        hash = self.hash_value(key) # 검색하는 키의 해시값
        p = self.table[hash] # 버킷을 주목
        
        for i in range(self.capacity):
            if p.stat == Status.EMPTY: 
                break
            elif p.stat == Status.OCCUPIED and p.key == key:
                return p
            hash = self.rehash_value(key)
            p = self.table[hash]
        
        return None
    
    def search(self, key: Any) -> Any:
        """키가 key인 원소를 검색하여 값을 반환"""
        p = self.search_node(key)
        if p is not None:
            return p.value # 검색 성공
        else:
            return None # 검색 실패
        
    def add(self, key: Any, value: Any) -> bool:
        """키가 key이고 값이 value인 원소를 추가"""
        if self.search(key) is not None: # 이미 등록된 키이면 False 반한
            return False
        
        hash = self.hash_value(key) # 추가하는 키의 해시값
        p = self.table[hash]
        
        for i in range(self.capacity):
            if p.stat == Status.EMPTY or p.stat == Status.DELETED:
                self.table[hash] = Bucket(key, value, Status.OCCUPIED)
                return True
            hash = self.rehash_value(key) # 재해시
            p = self.table[hash]
        return False # 해시 테이블이 가득 참
    
    def remove(self, key: Any) -> int:
        """키가 key인 원소를 삭제"""
        p = self.search_node(key)
        if p is None:
            return False # 이 키는 등록되어 있지 않음
        p.set_status(Status.DELETED)
        return True

    def dump(self) -> None:
        """해시 테이블을 덤프"""
        for i in range(self.capacity):
            print(f'{i:2} ', end='')
            if self.table[i].stat == Status.OCCUPIED:
                print(f'{self.table[i].key} ({self.table[i].value})')
            elif self.table[i].stat == Status.EMPTY:
                print('-- 미등록 --')
            elif self.table[i].stat == Status.DELETED:
                print('-- 삭제 완료 --')

    
