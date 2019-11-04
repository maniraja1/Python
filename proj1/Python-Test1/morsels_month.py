
import calendar,datetime
from datetime import date
class morsels_month():
    def __init__(self,year,month):
        self.__month = month
        self.__year = year
        self.__first_day = datetime.date(self.year,self.month,1)
        self.__last_day = datetime.date(self.year,self.month,calendar.monthrange(self.year,self.month)[1])

    def __str__(self):
        return f"Month({self.year},{self.month})"

    def __repr__(self):
        return f"Month({self.year},{self.month})"

    def __eq__(self, other):
        if self.year == other.year and self.month==other.month:
            return True
        else:
            return False

    def __lt__(self, other):
        if self.year < other.year:
            return True
        elif self.year == other.year and self.month < other.month:
            return True
        else:
            return False

    def __gt__(self, other):
        if self.year > other.year:
            return True
        elif self.year == other.year and self.month > other.month:
            return True
        else:
            return False

    def from_date(date1):
        return morsels_month(date1.year,date1.month)

    def strftime(self,*args):
        return datetime.date(year=self.year,month=self.month,day=self.first_day.day).strftime(*args)

    @property
    def month (self):
        return self.__month

    @month.setter
    def month(self,value):
        raise Exception("Cannot set value for month")

    @property
    def year(self):
        return self.__year

    @year.setter
    def year(self,value):
        raise Exception ("Cannot set value for year")

    @property
    def first_day(self):
        return self.__first_day

    @first_day.setter
    def first_day(self,value):
        raise Exception("Cannot set value for first_day")

    @property
    def last_day(self):
        return self.__last_day

    @last_day.setter
    def last_day(self,value):
        raise Exception("Cannot set value for last_day")

    def __hash__(self):
        return hash((self.year, self.month))


dec99 = morsels_month(1999,12)
oct99 = morsels_month(1999,10)

print(sorted([morsels_month(1998, 12), morsels_month(2000, 1), morsels_month(1999, 12)]))

feb99 = morsels_month(1999,2)
print(feb99)
print(feb99.last_day)

nye99 = date(1999, 12, 31)
dec99 = morsels_month.from_date(nye99)
print(dec99)
print(dec99.strftime('%b %Y'))

dec99.year=2000
print(dec99.year)
# dec99._morsels_month__year=2000
# print(dec99.year)



'''
1. One way to compare Year, Month is to use tuple comparison
return (self.year, self.month) == (other.year, other.month)
return (self.year, self.month) < (other.year, other.month)

2. This class decorator allows us to implement __eq__ and __lt__ and we'll get the other comparison methods for free.
from functools import total_ordering. 
@total_ordering
class Month:

3. Comparison operators in python3 are cumulative by default. This means that x >= y will call y < x if __ge__ isn't defined. 

4. First day & Last day can be properties instead of hard coded values. Setting them up as a property will calculate these dates each time they're called.

5. Note form_date does not need to be an instance method. So we should have declared as a @staticmethod or @classmethod.

6. Let's talk about __slots__ now. The __slots__ attribute is a way of saying "this class will only ever have these particular attributes, so use a tuple to store their values instead of a dictionary".

7. How to make class properties immutable
    1. _ & __. __ causes name mangling and should be avoided
    2. override __setattr__ * __delattr__. This will prevent you from setting the values in init for which you can use these methods from the base class object.
       super().__setattr__('year', year)
       super().__setattr__('month', month)

'''