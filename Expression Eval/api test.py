import time

import requests
import random
import multiprocessing
import timeit


# This code is to test the ms application which I have made
# It runs a set of random equations and triggers it
def thread_func(x):
    for j in range(10):
        endpoint = "http://localhost:8080/expressions"
        string_data = str(random.randint(1, 9)) + " * " + str(random.randint(1, 9))
        response = requests.post(endpoint, data=string_data, headers={"Content-Type": "text/plain"})
        print(response.status_code, response.content, f"part of {x}", string_data)
        for i in range(100):
            string_data = str(random.randint(1, 9)) + " * " + str(random.randint(1, 9))
            response = requests.post(endpoint, data=string_data, headers={"Content-Type": "text/plain"})
            print(response.status_code, response.content, f"part of {x}", string_data)
        response = requests.post(endpoint, data="end", headers={"Content-Type": "text/plain"})
        print(response.status_code, response.content, f"part of {x}", string_data)

    time.sleep(1)


def main():
    with multiprocessing.Pool(processes=50) as pool:
        pool.map(thread_func, [x for x in range(50)])


if __name__ == '__main__':
    execution_time = timeit.timeit(main, number=1)
    print(f"The function took {execution_time} seconds to execute.")
