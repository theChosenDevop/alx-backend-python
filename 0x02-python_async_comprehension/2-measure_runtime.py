#!/usr/bin/env python3
"""
    Defines 2-measure_runtime module
"""
import asyncio
import time


async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """ Measures the total runtime

    Returns:
        float: Total run time
    """
    startTime = time.time()
    await asyncio.gather(async_comprehension(),
                         async_comprehension(),
                         async_comprehension(),
                         async_comprehension())
    endTime = time.time()
    return endTime - startTime
