import time
from time import time as my_timer

print("\n********** Timer **********\n")



print("Starting timer...")
start_time = my_timer()

time.sleep(70)
end_time = my_timer()
print("Timer ended!")

print("Started at " + time.strftime("%X", time.localtime(start_time)))
print("Ended at " + time.strftime("%X", time.localtime(end_time)))

result = end_time - start_time
print(f"Time was {result}.")