import pytz, datetime

country = "Asia/Tokyo"

timezone = pytz.timezone(country)
local_time = datetime.datetime.now(tz=timezone)
utc_time = datetime.datetime.utcnow()

print(f"The time in {country} is {local_time}")
print(f"UTC time is {utc_time}.")


print("\n********** All timezones **********\n")

for x in pytz.all_timezones:
    print(x)
    
for x in sorted(pytz.country_names):
    print(x + ": " + pytz.country_names[x])