def get_days_of_month(i):
  day_list = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
  
  return day_list[i-1]

def count_days(start, end):
  start_month, start_day = start.split('/')
  end_month, end_day = end.split('/')
  start_month = int(start_month)
  start_day = int(start_day)
  end_month = int(end_month)
  end_day = int(end_day)
  
  day_count = 0
  if start_month == end_month:
    return end_day - start_day
  else:
    for i in range(start_month, end_month):
      day_count += get_days_of_month(i)
      return day_count + end_day - start_day
    
    
start = input('시작 월/일을 month/date 형식으로 입력하세요: ')
end = input('종료 월/일을 month/date 형식으로 입력하세요: ')

print(count_days(start,end))
