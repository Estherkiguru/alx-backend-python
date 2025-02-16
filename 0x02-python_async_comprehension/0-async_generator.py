#!/usr/bin/env python3
"""Module for  a coroutine called async_generator that takes no arguments."""

import asyncio
import random
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """Yields random number after waiting for 1 sec"""
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
