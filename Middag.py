import time

current_time = time.localtime()

if current_time.tm_hour >= 12 and current_time.tm_hour < 18:
    print("Het is middag!")
elif current_time.tm_hour < 12 and current_time.tm_hour >= 6:
    print("Het is ochtend!")
elif current_time.tm_hour >= 18 and current_time.tm_hour < 0:
    print("Het is avond!")
elif current_time.tm_hour < 6 and current_time.tm_hour >= 0:
    print("Het is nacht!")
