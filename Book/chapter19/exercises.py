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
