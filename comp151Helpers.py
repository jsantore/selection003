import time
import random

def get_credits_from_database(name='john'):
    time.sleep(5)
    num_credits = random.randint(15, 150)
    print(num_credits)
    return num_credits
