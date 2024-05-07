#!/usr/bin/env python3
"""
    Defines 1-concurrent_coroutines module
"""
import asyncio
from typing import List


wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """ The coroutine spawns the delay by n times

        Arguments
            max_delay {integer} -- maximum number of delay
            n {integer} -- an integer
    """
    coroutines = [wait_random(max_delay) for _ in range(n)]
    outputs = await asyncio.gather(*coroutines)
    return outputs
