import datetime
import time

from tqdm import tqdm

print(time.time())
print(time.ctime())
print(type(time.ctime()))

print(time.ctime(time.time()))


def calculate_product():
    product = 1
    for i in tqdm(range(1, 100001)):
        product *= i


# start = time.time()
# calculate_product()
# finish = time.time()
# print(f"Amount of time: {finish-start}")

# for _ in range(3):
#     print("Tick")
#     time.sleep(1)
#     print("Tock")
#     time.sleep(1)


now = datetime.datetime.now()
print(now)
print(type(now))
print(now.date())
print(now.hour)
print(now.today())

dt = datetime.datetime(2026, 1, 24, 23, 59, 59)
print(dt)
print(dt.year)
print(dt.month)
print(dt.day)

print(dt.hour)
print(dt.minute)
print(dt.second)

print(datetime.datetime.fromtimestamp(time.time()))
print(datetime.datetime.fromtimestamp(1000000000))

halloween_2026 = datetime.date(2026, 10, 31)
new_years_2027 = datetime.date(2027, 1, 1)

print(halloween_2026 > new_years_2027)
print(new_years_2027 - halloween_2026)

delta = datetime.timedelta(days=11, hours=10, minutes=9, seconds=8)
print(delta.days, delta.seconds, delta.microseconds)
print(delta.total_seconds())
print(delta)

thousand_days = datetime.timedelta(days=1000)
print(halloween_2026 + thousand_days)

oct_21st = datetime.datetime(2026, 10, 21)
about_thirty_years = datetime.timedelta(days=365 * 30)

print(oct_21st - about_thirty_years)
print(about_thirty_years * 2)

# Looping for a few years
# halloween_2039 = datetime.datetime(2039, 10, 31)
# while datetime.datetime.now() <= halloween_2039:
#     time.sleep(1)
#     print("Patience my man")

print(time.strftime("%Y/%m/%d %H%:%M:%S"))
print(time.strftime("%I:%M %p"))
print(oct_21st.strftime("%B of '%y'"))

string_date_1 = "October 21, 2026"
date_1 = datetime.datetime.strptime(string_date_1, "%B %d, %Y")
print(date_1)

string_date_2 = "2026/10/21 16:29:00"
date_2 = datetime.datetime.strptime(string_date_2, "%Y/%m/%d %H:%M:%S")
print(string_date_2)

string_date_3 = "October of '26'"
date_3 = datetime.datetime.strptime(string_date_3, "%B of '%y'")
print(date_3)

string_date_4 = "November of '63'"
date_4 = datetime.datetime.strptime(string_date_4, "%B of '%y'")
print(date_4)

string_date_5 = "November of '73'"
date_5 = datetime.datetime.strptime(string_date_5, "%B of '%y'")
print(date_5)
