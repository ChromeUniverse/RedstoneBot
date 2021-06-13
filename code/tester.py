"""
A functional demo of all possible test cases. This is the format you will want to use with your testing bot.

    Run with:
        python example_tests.py TARGET_NAME TESTER_TOKEN
"""

# module imports
import asyncio
import sys

# distest function/class imports
from distest import TestInterface
from distest import TestCollector
from distest import run_command_line_bot

# Discord class imports
from discord import Embed, Member, Status

# credentials
from bot_setup import (
  token,
  prefix,
  embedColor
)

from tester_setup import (
  target_id,
  tester_token,
  channel_id
)


# The tests themselves

test_collector = TestCollector()

# test `ping` command 
@test_collector()
async def test_ping(interface):
  await interface.assert_reply_contains(prefix + " ping", "Pong!")

# test `help` command with embed check
@test_collector()
async def test_help(interface):
  patterns = {"title": "Help Page"}
  await interface.assert_reply_embed_regex(prefix + " help", patterns)

# test invalid start commands
@test_collector()
async def test_invalid_start(interface):
  await interface.assert_reply_contains(prefix + " start", "Invalid")
  await interface.assert_reply_contains(prefix + " start 2", "Invalid")
  await interface.assert_reply_contains(prefix + " start 69", "Invalid")


# Actually run the bot

if __name__ == "__main__":  
  run_command_line_bot(    
    target      = int(target_id),
    token       = tester_token,
    channel_id  = int(channel_id),
    tests       = 'all',
    stats       = True,
    timeout     = 5,
    collector   = test_collector
  )