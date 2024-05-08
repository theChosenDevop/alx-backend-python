#!/usr/bin/env python3
"""
    Defines 2-measure_runtime module
"""
import asyncio
import time
from importlib import import_module as use


async_comprehension = use('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """ Measures the total runtime

    Returns:
        float: Total run time
    """
    startTime = time.time()
    await asyncio.gather(*(async_comprehension() for _ in range(4)))
    endTime = time.time()
    return endTime - startTime
