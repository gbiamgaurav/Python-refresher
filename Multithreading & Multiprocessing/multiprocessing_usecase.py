
import multiprocessing 
import math, sys, time 

# Increase the max digits for int conversion
sys.set_int_max_str_digits(100000)

# Function to compute factorial of a number
def compute_factorial(num):
    print(f"Computing factorial of {num}")
    result = math.factorial(num)
    print(f'Factorial of {num} is {result}')
    return result

if __name__ == "__main__":
    numbers = [5000, 6000, 7000, 8000]

    start_time = time.time()

    # Create a pool of worker processes
    with multiprocessing.Pool() as pool:
        results = pool.map(compute_factorial, numbers)

    end_time = time.time()

    print(f"Results: {results}")
    print(f"The execution took {end_time-start_time} seconds")