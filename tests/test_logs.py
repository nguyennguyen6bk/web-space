import ast
import asyncio
import json
import os
import sys
from playwright.async_api import async_playwright


import logging
from browser_use import Agent


import ast
import asyncio
import json
import sys

from playwright.async_api import async_playwright
from browser_use import Agent
from utils.logs_utils import logger


async def main(my_args):
    for i in my_args:
        print(f"Running test with argument: {i}")
        logger.info(f"Running test with argument: {i}")       

def parse_args(args):
    tasks = []
    for arg in args:
        if '-' in arg:
            start, end = arg.split('-')
            start = (int(start) if start.isdigit() else 0)
            end = (int(end) if end.isdigit() else 0)
            tasks.extend(range(start, end + 1))
        else:
            tasks.append(arg)
    return tasks

if __name__ == "__main__":
    if len(sys.argv) > 1:
        arg = sys.argv[1:]
    else:
        arg = ["1"]

    args = parse_args(arg)
    asyncio.run(main(args))

