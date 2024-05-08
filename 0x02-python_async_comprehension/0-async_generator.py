#!/usr/bin/env python3
"""
    Defines 0-async_generator module
"""
import asyncio
import random


async def async_generator() -> float:
    """Coroutine yields random numbers

    Returns:
        float: A float random numbers
    """
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
