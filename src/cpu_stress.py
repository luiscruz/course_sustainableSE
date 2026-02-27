import time

def fib(n):
    if n <= 1:
        return n
    return fib(n-1) + fib(n-2)

duration_minutes = 5   # change to 1 if needed
end_time = time.time() + duration_minutes * 60

print(f"Running CPU-intensive Fibonacci task for {duration_minutes} minutes...")

while time.time() < end_time:
    fib(35)   # 35–38 is usually heavy; adjust if too slow/fast

print("Finished.")