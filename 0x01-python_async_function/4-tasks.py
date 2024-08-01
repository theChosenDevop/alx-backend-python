#!/usr/bin/env python3
"""Task 4 module"""
import asyncio
from tying import List

task_wait_random = __import__('3-task').task_wait_random


def task_wait_random(max_delay: int) asyncio.Task:
    """Executes task_wait_random n times
    """
    wait_times = await asyncio.gather(
        *tuple(map(lambda_: task_wait_random(mmax_delay), range(n)))
    )
    return sorted(wait_times)
