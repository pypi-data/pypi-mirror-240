# -*- coding:utf-8 -*-
# Author: ranpeng
# Date: 2023/11/13

import time
import warnings

def timer(func):
    """time counter"""
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"{func.__name__} took {end_time - start_time:.2f} seconds to execute.")
        return result
    return wrapper

def memoize(func):
    """memorize func outcome"""
    cache = {}
    def wrapper(*args):
        if args in cache:
            return cache[args]
        result = func(*args)
        cache[args] = result
        return result
    return wrapper

def log_results(func):
    """log result in current work path"""
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        with open("results.log", "a") as log_file:
            log_file.write(f"{func.__name__} - Result: {result}\n")
        return result

    return wrapper

def suppress_errors(func):
    """catch func's exception and continue execution"""
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            print(f"Error in {func.__name__}: {e}")
            return None

    return wrapper

def retry(max_attempts, delay):
    """retry your func """
    def decorator(func):
        def wrapper(*args, **kwargs):
            attempts = 0
            while attempts < max_attempts:
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    print(f"Attempt {attempts + 1} failed. Retrying in {delay} seconds.")
                    attempts += 1
                    time.sleep(delay)
            raise Exception("Max retry attempts exceeded.")
        return wrapper
    return decorator

def debug(func):
    """print func arguments, help your debugging"""
    def wrapper(*args, **kwargs):
        print(f"Debugging {func.__name__} - args: {args}, kwargs: {kwargs}")
        return func(*args, **kwargs)
    return wrapper

def deprecated(func):
    """inform func will not longer update"""
    def wrapper(*args, **kwargs):
        warnings.warn(f"{func.__name__} is deprecated and will be removed in future versions.", DeprecationWarning)
        return func(*args, **kwargs)
    return wrapper