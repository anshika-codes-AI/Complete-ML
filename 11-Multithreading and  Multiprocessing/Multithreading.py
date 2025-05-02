### Multithreading
    ## when to use multithreading
        # I/O bound tasks = Tasks that spend more time waiting for i/o operations(e.g., file operation , network request).

        # Concurrent Execution = When you want to improve the throughout of your application by performing multiple operations concurrently.


import threading 
import time
def print_numbers():
    for i in range(5):
        time.sleep(2)
        print(f"Number : {i}")
    
def print_letters():
    for letter in 'abcde':
        time.sleep(2)
        print(f"Letter: {letter}")


## Create two threads.
t1 = threading.Thread(target = print_numbers)
t2 = threading.Thread(target = print_letters)
t = time.time()

## Thread start
t1.start()
t2.start()

## wait for the threads to complete
t1.join()
t2.join()

finished_time = time.time() - t
print(finished_time)