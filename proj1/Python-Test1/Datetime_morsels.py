import datetime
def is_over(age, dob):
    dob_date = datetime.datetime(int(dob.split('-')[0]),int(dob.split('-')[1]),int(dob.split('-')[2]))
    curr=datetime.datetime.now()

    x=(curr.year-dob_date.year)
    if(curr.month < dob_date.month):
        x -=1
    if(curr.month == dob_date.month and curr.day < dob_date.day):
        x -= 1
    if x==age:
        return True
    else:
        return False

from datetime import date, datetime
def is_over_soln1(age, date_string):
    today = date.today()
    born = datetime.strptime(date_string, '%Y-%m-%d').date()
    age_years_ago = today.replace(year=today.year - age)
    return born < age_years_ago

from datetime import datetime
def is_over_soln2(age, date_string):
    today = datetime.now()
    born = datetime.strptime(date_string, '%Y-%m-%d')
    age_years_ago = today.replace(year=today.year - age)
    return born < age_years_ago

''' TO work with Leap years'''
from datetime import date
def is_over_soln3(age, date_string):
    year, month, day = (int(s) for s in date_string.split('-'))
    today = date.today()
    return (year, month, day) < (today.year - age, today.month, today.day)

''' To work with Leap years'''
from datetime import datetime, timedelta
ONE_DAY = timedelta(days=1)
def is_over(age, date_string):
    today = datetime.now()
    born = datetime.strptime(date_string, '%Y-%m-%d')
    try:
        age_years_ago = today.replace(year=today.year - age)
    except ValueError:
        age_years_ago = (today + ONE_DAY).replace(year=today.year - age)
    return born < age_years_ago

def get_age(date_string):
    born = datetime.strptime(date_string, '%Y-%m-%d')
    today = datetime.now()
    shift = (today.month, today.day) < (born.month, born.day)
    return today.year - born.year - shift

''' Get Age in fraction'''
from datetime import date, datetime, timedelta
from fractions import Fraction

def get_birthday(birthdate, year):
    try:
        return birthdate.replace(year=year)
    except ValueError:
        day_after_birthdate = birthdate + timedelta(days=1)
        return day_after_birthdate.replace(year=year)


def get_age_soln2(date_string, exact=False):
    born = datetime.strptime(date_string, '%Y-%m-%d')
    today = datetime.now()
    shift = (today.month, today.day) < (born.month, born.day)
    age = today.year - born.year - shift
    if exact:
        days_since = today - get_birthday(born, born.year+age)
        days_until = get_birthday(born, born.year+age+1) - today
        return age + Fraction(days_since.days, (days_since + days_until).days)
    else:
        return age

print(is_over_soln1(18, '2000-2-29'))

