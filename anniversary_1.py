# datetime 라이브러리 : 날짜와 시간을 다루기 위한 다양한 기능 제공
# datetime 클래스 : 날짜와 시간에 대한 다양한 작업을 수행할 수 d있는 메서드 제공
'''
주요 특징
1. 날짜와 시간의 결합된 표현
2. 다양한 방법으로 날짜와 시간을 생성, 포맷팅 가능
3. 시간대 정보 처리
'''
from datetime import datetime

# 만난 지/결혼한 지 며칠인지 계산하기
# 현재 날짜와 시간 가져오기
now = datetime.now()
# 결혼일자 담은 wedding_day 객체 생성
wedding_day = datetime(2017, 7, 22)
wedding_days = now - wedding_day # 결혼 며칠 지났는지

# 아래처럼 사용하면 일수 뿐만 아니라 시간, 분 초 등의 정보도 함께 출력
# 우리 결혼한지 + 2542 days, 10:38:09.683759일 째
# print(f'우리 결혼한지 + {wedding_days}일 째')

# 일수만 출력하기 위해 days 속성 사용
print(f'우리 결혼한지 + {wedding_days.days}일 째')