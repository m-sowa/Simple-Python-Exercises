#Program counts down seconds spcified by the user

#introduction
print("Hello! Let me know how many seconds you want to wait and I will count them down or you!")

import time
seconds = int(input("\nNumber of seconds:"))
print()

while seconds != 0:
    print("You have", seconds, "seconds left")
    seconds = seconds - 1
    time.sleep(1)
print ("\nFinito!")

#ending
input("\n\nPress Enter to finish.")