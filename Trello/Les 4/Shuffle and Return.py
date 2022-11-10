import random

origineel = "Goedenmiddag"
random_woord = ''.join(random.sample(origineel, len(origineel)))
print(random_woord)
