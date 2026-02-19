import time


def fibonacci_warmup(seconds=300):
    """
    CPU warm-up to stabilize energy readings before measurement.
    Runs Fibonacci computation for the given number of seconds.
    Default: 5 minutes (300s) before the first run.
    """
    end = time.time() + seconds
    a, b = 0, 1
    while time.time() < end:
        a, b = b, a + b


if __name__ == '__main__':
    print(f'Starting {300}s warm-up...')
    fibonacci_warmup(seconds=300)
    print('Warm-up complete.')
