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
