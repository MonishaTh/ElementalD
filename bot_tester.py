import asyncio
import sys
from distest import TestCollector
from distest import run_interactive_bot, run_dtest_bot
from discord import Embed

test_collector = TestCollector()
created_channel = None

@test_collector()
async def combineTest(interface):
    await interface.assert_reply_contains("!combine fire earth", "fire+earth=Lava")    
    await interface.assert_reply_contains("!combine zzzzz, zzzzz", "Invalid combination")
    
    
    




















if __name__ == "__main__":
    run_dtest_bot(sys.argv, test_collector)