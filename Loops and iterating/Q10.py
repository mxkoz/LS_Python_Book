import random

# highest = 10
# number = random.randrange(highest + 1)
# print(number)

# while number != highest:
#     number = random.randrange(highest + 1)
#     print(number)

import random
highest = 10
while True:
    number = random.randrange(highest+1)
    if number == highest:
        break
    print(number)
    