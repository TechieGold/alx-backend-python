#!/user/bin/python3
"""
Module for asynchronous coroutine to wait for a random delay
Args:
    max_delay(int, optional): Mzximum delay in seconds. Default to 10.
Returns:
        float: Random delay between 0 and max_delay seconds (inclusive).
"""
import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """Asynchronous coroutine that waits for a random delay """
    wait = random.uniform(0, max_delay)
    await asyncio.sleep(wait)
    return (wait)
