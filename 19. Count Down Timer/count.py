import time

# To get current second: Take remainder of 60
# To get minute divide current time with 60 and take reminder of 60
# To get hours divide current time with 3600 and take remider of 24

my_time = int(input("Enter time in seconds: "))

for x in range(my_time, 0, -1):
    seconds = x % 60
    minutes = int((x/60)%60)
    hours = int((x/3600)%24)

    print(f"{hours:02}:{minutes:02}:{seconds:02}")
    time.sleep(1)

# print("TIME'S UP")