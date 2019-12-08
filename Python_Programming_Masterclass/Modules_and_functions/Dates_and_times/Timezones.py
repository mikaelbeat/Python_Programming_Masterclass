import time

print("The epoch on this system starts at " + time.strftime('%c', time.gmtime(0)))
print(f"The current timezone is {time.tzname[0]}, with an offset of {time.timezone}.")


print("\n********** Check is daylight saving time active **********\n")

if time.daylight != 0:
    print("Daylight saving time is in effect for this location!")
    print(f"The DST timezone is {time.tzname[1]}")
    
    
print("\n********** Get local time and UTC time **********\n")

local = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
utc = time.strftime('%Y-%m-%d %H:%M:%S', time.gmtime())
    
print(f"Local time is {local}")
print(f"UTC time is {utc}")


print("\n********** Get local time small **********\n")

local = time.strftime('%H:%M:%S', time.localtime())
    
print(f"Local time in hour, minutes and seconds -> {local}")
