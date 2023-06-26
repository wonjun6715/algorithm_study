# algorithm_study

## 알고리즘이란?
어떠한 문제를 해결하기 위해 정해 놓은 일련의 절차

## 리스트
원소를 변경할 수 있는 뮤터블(mutable) list형 객체
리스트는 연산자 [] 안에 원솔르 쉼표(,)로 구분하여 표기하여 생성

## 튜플
원소를 변경할 수 없는 이뮤터블(immutable) 자료형
튜플은 원소에 순서를 매겨 결합한 것으로 원소를 (,) 로 구분하여 나열한 뒤 결합 연산자 ()로 둘러싸는 방식으로 생성

## 검색 알고리즘
1. 선형 검색 : 직선 모양으로 늘어선 배열에서 검색하는 경우에 원하는 키값을 가진 원소를 찾을 때까지 맨 앞부터 스캔하여 순서대로 검색하는 알고리즘
2. 이진 검색 : 데이터가 정렬되어 있는 배열에서 특정한 원소를 찾는 알고리즘, 배열에 있는 중간의 임의의 값을 선택하여 찾고자 하는 값 key와 비교, 중간 값(pc)가 key보다 작으면 pc+1 ~ pr까지 범위를 좁힘, 큰 경우에는 pl ~ pc - 1까지 범위를 좁힘
3. 해시법 : 데이터를 저장할 위치를 간단하게 연산으로 구현하는 방법, 배열에서 각각의 원소 값을 배열의 크기로 나누어 원소에 접근할 때 기준 값(해시값)으로 함, 나머지를 구하는 연산 또는 그 연산을 응용할 때 주로 사용  

해결 방법 : 체인법, 오픈주소법
