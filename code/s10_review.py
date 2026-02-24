import random

roll = 0
while roll != 6:
    roll = random.randint(1, 6)
    print("Rolled:", roll)
    if roll > 3:
        print(' big roll!')
    else:
        print(' small roll!')

print("Got a 6!")

