
# Multiprocessing - When to use?

# High on CPU Bound Tasks - tasks that are heavy on CPU usage (eg. Mathematical Operations, data processing)
# Parallel Execution - Multiple cores of the CPU

import multiprocessing
import time 

def square_numbers():
    for i in range(5):
        time.sleep(2)
        print(f"Square: {i**2}")


def cube_numbers():
    for i in range(5):
        time.sleep(2)
        print(f"Cube: {i**3}")

if __name__ == "__main__":


    start_time = time.time()

    # Create process
    p1 = multiprocessing.Process(target=square_numbers)
    p2 = multiprocessing.Process(target=cube_numbers)

    # Start the process
    p1.start()
    p2.start()

    p1.join()
    p2.join()

    finished_time = time.time() - start_time
    print(f"Time took to execute this program:{finished_time: .4f} seconds")