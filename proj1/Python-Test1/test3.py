class human:
    def __init__(self,x):
        self._x = x
    def whoareyou(self):
        return self._x
    def method1(self):
        return type(self)

    def method2(self):
        return self.__class__.__name__

    def method3(self):
        return type(self)(self.whoareyou())

mani=human('mani')
print(mani.method1())
print(mani.method2())
print(mani.method3())


import calendar
print(calendar.weekday(2019, 7, 1))
c = calendar.Calendar(firstweekday=calendar.SUNDAY)


year = 2019; month = 10

monthcal = c.monthdatescalendar(year,month)
print(monthcal)
second_tuesday= [day for week in monthcal for day in week if
                day.weekday() == calendar.TUESDAY and
                day.month == month][2]
print(second_tuesday)

