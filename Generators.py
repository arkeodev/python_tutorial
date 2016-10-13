"""
Write a generator "trange", which generates a sequence of time tuples from start to stop
incremented by step. A time tuple is a 3-tuple of integers: (hours, minutes, seconds)

Example:
for time in trange((10, 10, 10), (13, 50, 15), (0, 15, 12) ):
        print(time)

will return
(10, 10, 10)
(10, 25, 22)
(10, 40, 34)
(10, 55, 46)
(11, 10, 58)
(11, 26, 10)
(11, 41, 22)
(11, 56, 34)
(12, 11, 46)
(12, 26, 58)
(12, 42, 10)
(12, 57, 22)
(13, 12, 34)
(13, 27, 46)
(13, 42, 58)
"""

def trange(start, stop, step):

    """
    trange(stop) -> time as a 3-tuple (hours, minutes, seconds)
    trange(start, stop[, step]) -> time tuple

    start: time tuple (hours, minutes, seconds)
    stop: time tuple
    step: time tuple

    returns a sequence of time tuples from start to stop incremented by step """

    current = list(start)
    while current < list(stop):
        yield tuple(current)
        seconds = step[2] + current[2]
        min_borrow = 0
        hours_borrow = 0
        if seconds < 60:
            current[2] = seconds
        else:
            current[2] = seconds - 60
            min_borrow = 1
        minutes = step[1] + current[1] + min_borrow
        if minutes < 60:
            current[1] = minutes
        else:
            current[1] = minutes - 60
            hours_borrow = 1
        hours = step[0] + current[0] + hours_borrow
        if hours < 24:
            current[0] = hours
        else:
            current[0] = hours -24

if __name__ == "__main__":
    for time in trange((10, 10, 10), (13, 50, 15), (0, 15, 12) ):
        print(time)
