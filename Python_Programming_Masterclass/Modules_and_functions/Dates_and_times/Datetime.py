import datetime

today = datetime.datetime.today()
now = datetime.datetime.now()
utc = datetime.datetime.utcnow()

print(f"\nDatetime today -> {today}")
print(f"\nDatetime now -> {now}")
print(f"\nDatetime UTC -> {utc}")