#!/usr/bin/env python3
"Measure runtime module"
import asyncio
import time

wait_n = __import__('1-concurrent_coroutines')


async def measure_time(n: int, max_delay: int) -> float:
    """measures the total execution time for wait_n

        Parameters:
            n [int]: integer
            max_delay [int]: maximum delay
        Returns: execution time
    """
    start_time = time.time()
    asyncio.run(wait_n(n, max_delay))
    return (time.time() - start_time) / n
