#!/usr/bin/env python3
"""
    Defines 0-basic_async_syntax module
"""
import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """ The function waits for a random delay between 0 and max_delay

        Arguments
            max_delay {integer} -- maximum delay

        Return
            [float] -- float random number
    """
    randValue = random.uniform(0.0, max_delay)
    await asyncio.sleep(randValue)

    return randValue
