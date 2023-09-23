# 과제 : 아래에 조건에 해당하는 코드를 구현하시오
# 이 파일에 그대로 코드 구현 후 byu0408@naver.com 메일로 파일을 전송할 것
# 기간 : 9월 25일 23시 59분 까지

# 아래에 주어진 리스트 외의 리스트는 문제해결을 위해 추가적으로 선언해도 됨

# 크기가 32인 October 라는 이름의 리스트가 있다.
# 0번째 인덱스는 False로 할당하고, 1 ~ 31번째 인덱스에는 10월 1일부터 10월 31일까지에 해당하는 요일의 첫글자 값으로 할당한다
# 예) October에 10번째 인덱스에는 "화" 라는 값이 들어간다.
import datetime
from pytimekr import pytimekr
import lunarcalendar
import holidays

October = list("" for x in range(32)) # October 리스트 초기화
October[0]=False

date = datetime.date(year=2023, month=10, day=1)

dict = {0:"월", 1:"화", 2:"수", 3:"목", 4:"금", 5:"토", 6:"일"}

patt = []
for _ in range(7):
    day_of_week = dict[date.weekday()]
    patt.append(day_of_week[0])
    date += datetime.timedelta(days=1)

patt_index=0

i=1
while i<len(October):
    October[i] = (patt[patt_index])
    patt_index=(patt_index + 1)%len(patt)
    i+=1
    if i >= 32:
        break


# 정수를 입력해서 문자열을 출력하는 함수 구현 (함수이름 : how_Dodw)
# 정수를 입력해서 해당하는 요일을 출력
# 예) how_dodw(10) 의 결과는 "화요일" 이 출력되야 함

def how_Dodw(day):
   print(October[day])


# 10월의 총 휴일이 몇 번 있는지 반환하는 함수 구현 (함수이름 : how_Holiday)
# 휴일은 토요일, 일요일, 달력에 빨간색으로 표기된 날
# 매개변수로는 위에서 선언한 October 리스트를 할당할 것이니, 리스트 형태임
# 아래의 구조를 변경하지 않는 선에서 구현

def how_Holiday(October) :
    holiday = 0
    holi = holidays.Korea()
    for i in range(1,32):
        day = f'2023-10-{i:02d}'
        if day in holi:
            holiday += 1



    # cal = lunarcalendar.LunarCalendar()
    # year = 2023
    # month = 10
    # for day in range(1, 32):
    #     date = datetime.date(year, month, day)
    #     if cal.is_holiday(date):
    #         October[day - 1] = '빨'
            
    for dodw in October:
        if dodw == '토' or dodw == '일':
            holiday += 1
        
        
    return holiday # 반환 값은 11이 되어야 함


how_Dodw(11) # "수요일"
how_Dodw(21) # "토요일"
print("10월의 휴일 횟수 :", how_Holiday(October), "번") # 10월의 휴일 횟수 : 11번