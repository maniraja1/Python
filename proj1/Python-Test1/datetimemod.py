import datetime
import pytz
from tzlocal import get_localzone


### naive date time, not aware of timezone and other additional info
### aware date time, has extra info

d = datetime.date(2018,5,22)
print(d)

d1=datetime.date.today()
print(d1)

print(d1.day)
print(d1.year)
print(d1.month)
print(d1.weekday())
print(d1.isoweekday())

tdelta=datetime.timedelta(days=7)
print(tdelta)

print(datetime.date.today()+tdelta)
print(datetime.date.today()-tdelta)

datediff=datetime.date.today()-datetime.date(2018,5,1)
print(datediff)
print(datediff.total_seconds())



t=datetime.time(22,30,30)
print(t)


dt=datetime.datetime(2018,5,22,22,34,56,100)
print(dt)
print(dt.date())
print(dt.time())
print(dt.today())
tdelta=datetime.timedelta(days=7)
print(dt+tdelta)
print(dt-tdelta)


print(datetime.datetime.today())
print(datetime.datetime.now())
print(datetime.datetime.utcnow())


tz=datetime.datetime(2018,5,22,22,34,56,100,tzinfo=pytz.utc)
print(tz)
print(datetime.datetime.utcnow().replace(tzinfo=pytz.utc))


#### You can create a timezone aware datetime by passing timezone info
#### datetime.datetime()  produces incorrect offset same as today() does.
print("custom dates with tz info")
dt_pac = datetime.datetime(2018,5,22,22,00,00,000,tzinfo=pytz.timezone('US/Pacific'))
print(dt_pac)
dt_cen = datetime.datetime(2018,5,22,22,00,00,000,tzinfo=pytz.timezone('US/Central'))
print(dt_cen)

#### If you want to set a date and have the right timezone offset displayed here is what you do.
#### Get  the local timezone and then set the date by localizing  your local timezone
#### Using this needs "from tzlocal import get_localzone" pip install tzlocal
tz1 = get_localzone()
date =  tz1.localize(datetime.datetime(2018,5,22,22,00,00,000))
print("custom date with tzinfo and displaying correct offset")
print(date)

print("custom date with tzinfo and displaying correct offset method#2")
tz2 = pytz.timezone('US/Pacific')
dt= tz2.localize(datetime.datetime.now())
print(dt)


### Now accepts timezone in the constructor. Today and UTCNow you cannot pass tz in the constructore but can use the replace method
### Below example today produces an incorrect offset. Always use now for timezone info
print("Using Now method: ")
print(datetime.datetime.now(tz=pytz.timezone('US/Pacific')))
print('Using Today method: ')
print(datetime.datetime.today().replace(tzinfo=pytz.timezone('US/Pacific'))) ### This produces a wrong offset. Use Now for accurate tz offset
print(get_localzone().localize(datetime.datetime.today())) ### This fixes the offset in the step above
print('Using UTCNow method: ')
print(datetime.datetime.utcnow().replace(tzinfo=pytz.utc))

#### This will print the current UTC date
print("Current UTC date")
print(datetime.datetime.now(tz=pytz.utc))
print(datetime.datetime.utcnow().replace(tzinfo=pytz.utc))

#### Both the below produces the same output.
print("Converting dates to central time")
print(datetime.datetime.now(tz=pytz.utc).astimezone(pytz.timezone('US/Central')))
print(datetime.datetime.now(tz=pytz.timezone('US/Pacific')).astimezone(pytz.timezone('US/Central')))

'''
#### enumnerate all the availale  timezone
for i in pytz.all_timezones:
    print(i)
'''
#### Converting naive time to a timezone aware time and convert to a diferent timezone
print('Converting naive time to a different timezone')
dt=datetime.datetime.now()
tz = pytz.timezone('US/Pacific')
dt= tz.localize(dt)
print(dt)
print(dt.astimezone(pytz.timezone('US/Eastern')))

