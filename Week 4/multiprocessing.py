# THIS SAME CAN BE DONE WITH THE MULTIPROCESSING TOO LETS SEE HOW HERE WE USE THE PROCESS POLL EXECUTER
from concurrent.futures import ProcessPoolExecutor, as_completed
import time

def square_number(number):
    try:
        time.sleep(2)
        return f"Square: {number * number}"
    except Exception as e:
        return f"Error processing number {number}: {e}"

numbers=[1,2,3,4,5,6,7,8,9,11,2,3,12,14]

with ProcessPoolExecutor(max_workers=3) as executor:
    futures = [executor.submit(square_number, number) for number in numbers]

for future in as_completed(futures):
    print(future.result())