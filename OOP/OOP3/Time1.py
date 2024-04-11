class Time:
    """
    Represents the time of day.

    attributes: hour, minute, second
    """


def int_to_time(seconds):
    """Makes a new Time object.

    seconds: int seconds since midnight.

    It is a helper function.
    """
    time = Time()
    minutes, time.second = divmod(seconds, 60)
    time.hour, time.minute = divmod(minutes, 60)
    return time
