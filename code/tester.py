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
  embedColor,
)

from tester_setup import (
  prefix,
  target_id,
  channel_id,
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


# test `time` command with embed check
@test_collector()
async def test_time(interface):
  patterns = {"title": "Server locations & Queue waiting times"}
  await interface.assert_reply_embed_regex(prefix + " time", patterns)
  


# test status command with embed check
@test_collector()
async def test_status(interface):
  patterns = {"description": "Server name:"}
  await interface.assert_reply_embed_regex(prefix + " status", patterns)



# test invalid start commands
@test_collector()
async def test_invalid_start(interface):
  await interface.assert_reply_contains(prefix + " start", "Invalid")
  await interface.assert_reply_contains(prefix + " start 2", "Invalid")
  await interface.assert_reply_contains(prefix + " start 69", "Invalid")


# test reset command with embed check
@test_collector()
async def test_reset(interface):
  await interface.assert_reply_contains(prefix + " reset", "Successfully unlinked")


# test invalid setup commands
@test_collector()
async def test_invalid_setup(interface):
  # simple replies
  await interface.assert_reply_contains(prefix + " setup", "!redstone setup [IP address]")
  await interface.assert_reply_contains(prefix + " setup whatever", "!redstone setup [IP address]")
  # embed replies
  patterns = {"title": "Incorrect server IP."}  
  await interface.send_message(prefix + " setup justarandomIP.ploudos.me")
  await interface.get_delayed_reply(10, interface.assert_embed_regex, patterns)
  # await interface.assert_reply_contains(prefix + " setup justarandomIP.ploudos.me", "Running setup... please wait.")


# test valid setup command
@test_collector()
async def test_setup(interface):
  patterns = {"title": "Setup successful!"}  
  await interface.send_message(prefix + " setup " + sys.argv[2])
  await interface.get_delayed_reply(10, interface.assert_embed_regex, patterns)

# test valid start command
@test_collector()
async def test_start(interface):  
  await interface.assert_reply_contains(prefix + " start 1", "Nuremberg")
  await interface.get_delayed_reply(10, interface.assert_message_contains, 'Activation successful')


# test exit command
@test_collector()
async def test_exit(interface):  
  await asyncio.sleep(10)
  await interface.assert_reply_contains(prefix + " exit", "queue")
  await interface.get_delayed_reply(15, interface.assert_message_contains, 'Successfully left the queue')



# Actually run the bot

if __name__ == "__main__":  
  run_command_line_bot(    
    target      = int(target_id),
    token       = sys.argv[1],
    channel_id  = int(channel_id),
    tests       = 'all',
    stats       = True,
    timeout     = 5,
    collector   = test_collector
  )