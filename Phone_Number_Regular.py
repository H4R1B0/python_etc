"""
중고나라 같은 게시판에서 다양한 형태로 표현되는 핸드폰 번호를 볼 수 있는데 
이를 찾기 위한 정규식입니다.
"""
import re

# 0부터 9까지 각각 비슷한 문자 리스트
arr = [[] for _ in range(10)]
arr[0] = ['0','o','O','ㅇ','영','공']
arr[1] = ['1','i','l','I','!','일','/']
arr[2] = ['2','ㄹ','Z','z','이']
arr[3] = ['3','삼']
arr[4] = ['4','사']
arr[5] = ['5','오','ㅗ','s','S']
arr[6] = ['6','육','G','b']
arr[7] = ['7','칠','ㄱ']
arr[8] = ['8','팔','B']
arr[9] = ['9','구','g','q']

# 010 부분과 4자리 번호 정규식 글자
first, second = '',''

# 010 정규식
first = '(['+'|'.join(arr[0])+'])(['+'|'.join(arr[1])+'])(['+'|'.join(arr[0])+'])'

# 4자리 정규식
for i in range(10):
    second+=''.join(arr[i])
second = '([' + second + ']{4})'

# 패턴 생성
pattern = '^' + first + '-?' + second + '-?' + second + '$'

p = re.compile(pattern)

# 비교를 원하는 텍스트
if p.match('영1O-칠2공o-!영1오'):
    print('매치')
else:
    print('매치 안됨')
        
