#!/usr/bin/env python3


import time
import logging

logging.basicConfig(filename='log.txt', level=logging.INFO, format='%(message)s')


def compare_strings_withlog(str1, str2):
    start_time = time.perf_counter_ns()  
    res = compare_strings(str1, str2)
    end_time = time.perf_counter_ns()  
    execution_time = end_time - start_time
    logging.info(f"{str2}, Execution time: {execution_time} nanoseconds")
    return res


def compare_strings(str1, str2):
    

    if len(str1) != len(str2):
        return False
    
    for i in range(len(str1)):
        time.sleep(0.0001)
        if str1[i] != str2[i]:
            return False

    return True
