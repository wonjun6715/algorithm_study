# 포인터로 연결 리스트 구현하기(혼자서)

from __future__ import annotations
from typing import Any, Type

class Node:
    """연결 리스트용 노드 클래스"""
    def __init__(self, data: Any = None, next: Node = None):
        self.data = data
        self.next = next
        
class LinkedList:
    """연결 리스트 클래스"""
    def __init__(self) -> None:
        self.no = 0 # 노드의 개수
        self.head = None # 머리 노드
        self.current = None # 주목 노드
        
    def __len__(self) -> int:
        """연결 리스트의 노드의 개수를 반환"""
        return self.no
    
    def search(self, data: Any) -> int:
        """data와 값이 같은 노드를 검색(인덱스 반환)"""
        cnt = 0
        ptr = self.head
        while ptr is not None:
            if ptr.data == data: # 검색 노드를 발견한 경우
                self.current = ptr
                return cnt 
            else:
                cnt += 1
                ptr = ptr.next
        return -1 # 검색 조건을 만족하는 노드를 발견하지 못하고 꼬리 노드까지 왔을 경우
    
    def __contains__(self, data: Any) -> bool:
        """데이터가 포함되어 있는지 판단"""
        return self.search(data) >= 0
    
    def add_first(self, data: Any) -> None:
        """맨 앞에 노드를 삽입"""
        ptr = self.head # 삽입하기 전의 머리 노드
        self.head = self.current = Node(data, ptr)
        self.no += 1
        
    def add_last(self, data: Any) -> None:
        """맨 끝에 노드를 삽입"""
        if self.head is None:
            self.add_first(data)
        else:
            ptr = self.head
            while ptr.next is not None:
                ptr = ptr.next
            ptr.next = self.current = Node(data, ptr)
            self.no += 1
    
    def remove_first(self) -> None:
        """머리 노드를 삭제"""
        if self.head is not None:
            self.head = self.current = self.head.next
        self.no -= 1
        
    def remove_last(self) -> None:
        """꼬리 노드를 삭제"""
        if self.head is not None:
            if self.head.next is None:
                self.remove_first()
            else:
                ptr = self.head
                pre = self.head
                while ptr.next is not None:
                    pre = ptr
                    ptr = ptr.next
                pre.next = None
                self.current = pre
                self.no -= 1
                
    def remove(self, p: Node) -> None:
        """노드 p를 삭제"""
        if self.head is not None:
            if p is self.head:
                self.remove_first()
            else:
                ptr = self.head
                
                while ptr.next is not p: # p의 이전까지 ptr.next로 이동
                    ptr = ptr.next
                    if ptr is None:
                        return
                ptr.next = p.next
                self.current = ptr
                self.no -= 1
                
    def remove_current_node(self) -> None:
        """주목 노드를 삭제"""
        self.remove(self.current)
        
    def clear(self) -> None:
        """전체 노드를 삭제"""
        while self.head is not None:
            self.remove_first()
        self.current = None
        self.no = 0
        
    def next(self) -> bool:
        """주목 노드를 한 칸 뒤로 이동"""
        if self.current is None or self.current.next is None:
            return False
        self.current = self.current.next
        return True
    
    def print_current_node(self) -> None:
        """주목 노드를 출력"""
        if self.current is None:
            print('주목 노드가 존재하지 않습니다.')
        else:
            print(self.current.data)
            
    def print(self) -> None:
        """모든 노드를 출력"""
        ptr = self.head
        
        while ptr is not None:
            print(ptr.data)
            ptr = ptr.next