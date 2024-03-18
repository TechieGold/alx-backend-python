#!/usr/bin/env python3
"""
Module for asynchronous routine that spawns wait_random n times
Args:
    n(int): Number of times to spawn wait_random.
    max_delay(int): Maximum delay in seconds.
Returns:
    list: List of delays (float values) in ascending order.
"""
import asyncio
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> list[float]:
    """ Asynchronous routine that spawns wait_random n times """
    waits = []

    tasks = [wait_random(max_delay) for _ in range(n)]
    for task in asyncio.as_completed(tasks):
        wait = await task
        waits.append(wait)

    return (waits)
