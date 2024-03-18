#!/usr/bin/python3
"""
Module that creates an asyncio.Task for wait_random with the given max_delay.
Args:
    max_delay(int): Maximum delay in seconds.
Returns:
    asyncio.Task: Task object for wait_random coroutine.
"""
import asyncio
wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """ Create an asyncio.Task for wait_random with the given max_delay. """
    task = asyncio.create_task(wait_random(max_delay))
    return (task)
