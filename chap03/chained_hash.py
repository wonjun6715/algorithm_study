# 체인법으로 해시 함수 구현하기
# 체인법이란? : 해시 테이블에서 저장할 버킷이 중복될 때(해시 충돌) 연결리스트(체인 모양)로 관리 하는 것

from __future__ import annotations
from typing import Sequence, Any
import hashlib

class Node:
    """해시를 구성하는 노드"""
    
    def __init__(self, key: Any, value: Any, next: Node) -> None: # key, value, next를 전달 받음
        """초기화"""
        self.key = key # 키
        self.value = value # 값
        self.next = next # 뒤쪽 노드를 참조
        
class ChainedHash:
    """체인법으로 해시 클래스 구현"""
    
    def __init__(self, capacity: int) -> None:
        """초기화"""
        self.capacity = capacity # 해시 테이블의 크기를 지정
        self.table = [None] * self.capacity # 해시 테이블(리스트)을 선언
        
    def hash_value(self, key: Any) -> int:
        """해시값을 구함"""
        if isinstance(key, int):
            return key % self.capacity
        return(int(hashlib.sha256(str(key).encode()).hexdigest(), 16) % self.capacity) # key 값이 int형이 아닌 경우 형변환을 해야함

    def search(self, key: Any) -> Any:
        """키가 key인 원소를 검색하여 값을 반환"""
        hash = self.hash_value(key) # 검색하는 key의 해시값
        p = self.table[hash]
        
        while p is not None:
            if p.key == key:
                return p.value # 검색 성공
            p = p.next # 검색이 안되면 뒤쪽 노드를 주목
        
        return None # 검색 실패
    
    def add(self, key: Any, value: Any) -> bool:
        """키가 key이고 값이 value인 원소를 추가"""
        hash = self.hash_value(key) # 추가하는 key의 해시값을 구함
        p = self.table[hash] # 노드를 주목
        
        while p is not None:
            if p.key == key: # 이미 key값이 들어있다면
                return False
            p = p.next # 뒤쪽 노드를 주목
            
        temp = Node(key, value, self.table[hash])
        self.table[hash] = temp # 노드를 추가
        return True
    
    def remove(self, key: Any) -> bool:
        hash = self.hash_value(key) # 삭제할 key의 해시값
        p = self.table[hash] # 노드를 주목
        pp = None # 바로 앞의 노드를 주목
        
        while p is not None:
            if p.key == key: # 키를 발견하면 아래를 실행
                if pp is None:
                    self.table[hash] = p.next
                else:
                    pp.next = p.next # 키 삭제 성공
                return True
            pp = p 
            p = p.next # 뒤쪽 노드를 주목
        return False
    
    def dump(self) -> None:
        """해시 테이블을 덤프(통째로 출력)"""
        for i in range(self.capacity):
            p = self.table[i]
            print(i, end='')
            while p is not None:
                print(f'  -> {p.key} ({p.value})', end='')
                p = p.next
            print()