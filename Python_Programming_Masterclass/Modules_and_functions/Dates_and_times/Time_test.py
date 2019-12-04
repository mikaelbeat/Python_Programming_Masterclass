
import time
from time import time as my_timer

print("Starting time calculator")
#time.sleep(3)

start_time = 13:39:58
time.sleep(3)

end_time = my_timer()

print("Started at " + time.strftime("%X", time.localtime(start_time)))
print("Ended at " + time.strftime("%X", time.localtime(end_time)))

result = end_time - start_time

print(f"Your reaction time was {result}.")