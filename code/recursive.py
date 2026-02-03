import time


def groundhog_day():
    """A function that prints 'groundhog day' every second indefinitely."""
    print('Did you mean: groundhog day?')
    
    time.sleep(1)
    groundhog_day()


groundhog_day()