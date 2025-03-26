
# Multithreading - when to use ?
# I/O Tasks - Tasks that spend more time waiting for I/O operations (eg. file operations, network requests)
# Concurrent Execution: when you want to improve the throughput of your application by performing multiple operations concurrently

import threading
import time 

def print_numbers():
    for i in range(5):
        time.sleep(2)
        print(f"Number: {i}")

def print_letter():
    for letter in "abcde":
        time.sleep(2)
        print(f"Letter: {letter}")

# Multithreading
t1 = threading.Thread(target=print_numbers)
t2 = threading.Thread(target=print_letter)


start_time = time.time()
#print_numbers()
#print_letter()

# start the thread
t1.start()
t2.start()

# Wait for thread to complete

t1.join()
t2.join()

finished_time = time.time() - start_time
print(f"Time took to execute this program:{finished_time: .4f} seconds")