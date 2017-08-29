""" Tuple이란?
튜플(Tuple)은 몇 가지 점을 제외하곤 리스트와 거의 비슷하며 리스트와 다른 점은 다음과 같다.
- 리스트는 [와 ]으로 둘러싸지만 튜플은 (와 )으로 둘러싼다.
리스트는 그 값의 생성 삭제 수정이 가능하지만 튜플은 그 값을 바꿀 수 없다.
"""

# 튜플
t1 = ()
t2 = (1,) # 한 개의 요소만을 가질 때에는 요소 뒤에 콤마를 반드시 붙여야 한다.
t3 = (1, 2, 3)
t4 = 1, 2, 3 # 괄호를 생략해도 된다.
t5 = ('a', 'b', ('ab', 'cd'))

# 인덱싱하기
t1 = (1, 2, 'a', 'b')
print(t1[0]) # 1
print(t1[3]) # 'b'

# 슬라이싱하기
t1 = (1, 2, 'a', 'b')
print(t1[1:]) # (2, 'a', 'b') # index 1부터 마지막까지

# 튜플 더하기
t2 = (3, 4)
print(t1 + t2) # (1, 2, 'a', 'b', 3, 4)

# 튜플 곱하기
print(t2 * 3) # (3, 4, 3, 4, 3, 4)