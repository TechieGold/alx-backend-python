#!/usr/bin/env python3
""" 0-async_generator.py """
import asyncio
import random
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """ Loop 10 times and yield random number btw 0 and 10."""
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.random() * 10
