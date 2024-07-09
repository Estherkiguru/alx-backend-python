#!/usr/bin/env python3
"""Module for  a coroutine called async_generator that takes no arguments."""

import asyncio
import random


async def async_generator():
    """Yields random number after waiting for 1 sec"""
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
