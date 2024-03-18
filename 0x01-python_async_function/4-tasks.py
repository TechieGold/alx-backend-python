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
from typing import List

task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """ Asynchronous routine that spawns wait_random n times """
    waits = await asyncio.gather(
        *tuple(map(lambda _: task_wait_random(max_delay), range(n)))
    )

    return sorted(waits)
