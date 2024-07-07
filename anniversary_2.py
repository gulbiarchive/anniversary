# 결혼 날짜 입력받기
from datetime import datetime


now = datetime.now()

# 사용자로부터 결혼 날짜 입력 받기(년 월 일 형식
wedding_day_input = input('결혼 날짜 입력(예: 2017 7 22) : ')
year, month, day = map(int, wedding_day_input.split())
wedding_day = datetime(year, month, day)

wedding_days = now - wedding_day
print(f'우리 결혼한지 + {wedding_days.days}일 째')