# 문자열 검색법
## 문자열 검색이란?
- 어떤 문자열 안에 다른 문자열이 포함되어 있는지 검사하고, 만약 포함되어 있다면 어디에 위치해 있는지 찾아내는 것을 말함
- 검색되는 쪽의 문자열을 텍스트(text), 찾아내는 문자열을 패턴(pattern)이라고 함

## 브루트 포스법
- 선형 검색을 단순하게 확장한 알고리즘이라서 단순법 이라고도 함
- txt 안에 pat가 여러 번 포함될 경우에는 가장 앞쪽에 위치한 인덱스를 반환함. 실패할 경우 -1 반환

## KMP법
- 브루트 포스법과 달리 KMP법은 검사한 결과를 효율적으로 사용할 수 있는 알고리즘
- 검사했던 결과를 버리지 않고 효율적으로 활용하는 알고리즘
- 텍스트와 패턴 안에서 겹치는 문자열을 찾아내 검사를 다시 시작할 위치를 구하여 패턴의 이동을 되도록이면 크게하는 알고리즘
- ‘몇 번째 문자부터 다시 검색할지 값을 표로 만들어서 문제를 해결함
- 건너뛰기표(skip table)을 작성

## 보이어 무어법
- KMP법보다 더 효율적이어서 실제 문자열 검색에서 널리 사용하는 알고리즘
- 패턴의 끝 문자에서 시작하여 앞쪽을 향해 검사를 수행
- 이 과정에서 일치하지 않는 문자를 발견하면 미리 준비한 표를 바탕으로 패턴이 이동하는 값을 결정