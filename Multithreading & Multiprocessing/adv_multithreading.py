
# Multithreading with thread pool executor

from concurrent.futures import ThreadPoolExecutor
import time 

def print_numbers(num):
    time.sleep(1)
    return f"Number: {num}"

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]

with ThreadPoolExecutor(max_workers=3) as executor:
    results = executor.map(print_numbers, numbers)

for result in results:
    print(result)