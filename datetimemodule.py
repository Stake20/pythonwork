import datetime


today = datetime.date.today()
print(today)

birthday = datetime.date(1997, 4, 15)
print(repr(birthday))
print(birthday)

# find days since birth
days_since_birth = (today - birthday).days
print(days_since_birth)

# adding 10 days to current day
tdelta = datetime.timedelta(days=10)
print(today + tdelta)

print(today.month)
print(today.day)
print(today.weekday())

print(datetime.time(7, 2, 20, 15))
# datetime.date (Y, M, D)
# datetime.time (h, m, s, ms)
# datetime.datetime (Y, M, D, h, m, s, ms)

# add 10 hours to current day
hour_delta = datetime.timedelta(hours=10)
print(datetime.datetime.now() + hour_delta)


# using timezones, first i have to install pip module ( pip install pytz )
# import pytz
# print(datetime.datetime.now(tz=pytz.UTC))
# datetime_today = datetime.datetime.now(tz=pytz.UTC)
# datetime_pacific = datetime_today.astimezone(pytz.timezone("US/Pacific"))
# print(datetime_pacific)
# for tz in pytz.all_timezones:
#    print(tz)

# String Formatting with dates
# 2020-10-13 -> October 13, 2020
# strftime (f - formatting)
print(today.strftime('%B %d, %Y'))

# October 13, 2020 -> datetime(2020-10-13)
# strptime (p = parsing)
datetime_thing = datetime.datetime.strptime('October 13, 2020', '%B %d, %Y')
print(repr(datetime_thing))
print(datetime_thing)









