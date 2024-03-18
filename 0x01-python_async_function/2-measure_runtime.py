#!/usr/bin/env python3
"""
Module that measure the average execution time for wait_n.

Args:
    n(int): Number of times to spawn wait_random.
    max_delay(int): maximum delay in seconds.
"""
import asyncio
import time
wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """ Measures the average execution time for wait_n(n, delay)."""
    start_time = time.time()
    asyncio.run(wait_n(n, max_delay))
    end_time = time.time()

    return(end_time - start_time) / n
