#!/usr/bin/env python3
"""
    Defines 0-async_generator module
"""
import asyncio
import random
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """Coroutine yields random numbers

    Returns:
        float: A float random numbers
    """
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
