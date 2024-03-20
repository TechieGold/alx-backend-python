#!/usr/bin/env python3
""" 2-measure_runtime.py """
import asyncio
import time
from importlib import import_module
async_comprehension = import_module(
    '1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """ Executes async_comprehension 4 times and measures the
    total execution time. """
    start_time = time.time()
    await asyncio.gather(*(async_comprehension() for _ in range(4)))
    end_time = time.time()
    return (end_time - start_time)
