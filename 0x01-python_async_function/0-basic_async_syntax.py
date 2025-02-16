#!/usr/bin/env python3
"""Module for an asynchronous coroutine that takes in an integer argument"""

import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """Waits for random delay btwn 0 & max_delay"""
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
