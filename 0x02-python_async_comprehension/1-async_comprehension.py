#!/usr/bin/env python3
"""
    Defines 1-async_comprehension module
"""
from typing import List


async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """Collects ten random float numbers using async comprehension

    Returns:
        List[float]: List of random float numbers
    """
    try:
        return [randomNumber async for randomNumber in async_generator()]
    except Exception as e:
        print(f"An error occurred: {e}")
        return []
