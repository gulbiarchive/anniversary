from datetime import datetime, timedelta

plus_days = 2000
wedding_day = datetime(2017, 7, 22)

'''
timedelta 사용 이유
datetime 객체는 직접적으로 날짜를 더하거나 뺄 수 없다.
따라서 timedelta를 사용하여 날짜를 더하거나 뺴서 새로운 datetime 객체를 생성하는 방법을 사용한다.

예)
wedding_day = datetime(2017, 7, 22)
wedding_day += 2000 # error
'''
the_day = wedding_day + timedelta(days=plus_days)
print(f'우리 결혼한지 +{plus_days}일은 {the_day.year}년 {the_day.month}월 {the_day.day}일')