import time
import logging


logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def time_logger(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        execution_time = end_time - start_time
        logging.info(f"Executed {func.__name__} in {execution_time:.4f} seconds")
        return result
    return wrapper


@time_logger
def expensive_task(n):
    result = 0
    for i in range(n):
        result += sum(j * j for j in range(1000))
    return result

n = int(input("Enter the value of n: "))
print(f"Result of expensive task: {expensive_task(n)}")