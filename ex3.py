import datetime


x = datetime.datetime(2020, 6, 10)
print('******************************')
print('Today\'s date: {} {}/{}/{}'
.format(x.strftime('%a'),x.year,x.month,x.day))
#print(x.strftime('%A'))

print(x)