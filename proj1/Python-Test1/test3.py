from enum import IntEnum
from datetime import datetime,timedelta

class Weekday(IntEnum):
    Monday=1
    Tuesday=2
    Wednesday=3
    Thursday=4
    Friday=5
    Saturday=6
    Sunday=7

class NextDate:

    def __init__(self, day,after_today=True):
        self.current_day = datetime.now().isoweekday()
        self.day=day
        self.days_until = self.DaysUntil(day,after_today)
        self.date = self.GetNextDate()

    def DaysUntil(self, day,after_today):
        if self.current_day > day:
            return (day+7)-self.current_day
        elif self.current_day == day and after_today:
            return (day + 7) - self.current_day
        else:
            return day-self.current_day

    def GetNextDate(self):
        return datetime.now()+timedelta(self.days_until)

    def __str__(self):
        return f"str(NextDate(Weekday.{Weekday(self.day).name}))"






print(Weekday.Thursday.value)
print(Weekday.Monday.value)
print(Weekday(1).name)

next_friday = NextDate(Weekday.Friday)
next_thursday = NextDate(Weekday.Thursday,False)
print(next_thursday.days_until)
print(next_thursday.date)


print(str(NextDate(Weekday.Friday)) == str(NextDate(Weekday.Friday)))
