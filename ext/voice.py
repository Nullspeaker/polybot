import sys
import asyncio
import discord
from os import path
sys.path.append(path.dirname(path.dirname(path.abspath(__file__))).replace("ext/",""))
from utils import *

if not discord.opus.is_loaded():
    discord.opus.load_opus('opus')

async def digest(message,bot):
    if message.content[0] in bot.commandPrefix:
        tokens=tokenize(message)
        tokens[0]=tokens[0][1:]
        print(tokens)
        if isMatch(tokens[0],"voice"):
            if isMatch(tokens[1],"jc"):
                if bot.is_voice_connected(
                        message.channel.server
                        ):
                    pass
                else:
                    await bot.join_voice_channel(
                        message.author.voice_channel
                        )
                vc = bot.voice_client_in(
                        message.channel.server
                        )
                player = await vc.create_ytdl_player(
                        "https://www.youtube.com/watch?v=ggKeB9OOkRY"
                        )
                player.start()
            elif isMatch(tokens[1],"rr2"):
                if bot.is_voice_connected(
                        message.channel.server
                        ):
                    pass
                else:
                    await bot.join_voice_channel(
                        message.author.voice_channel
                        )
                vc = bot.voice_client_in(
                        message.channel.server
                        )
                player = await vc.create_ytdl_player(
                        "https://www.youtube.com/watch?v=0NlfQdH5MSg"
                        )
                player.start()
            elif isMatch(tokens[1],"purpose"):
                if bot.is_voice_connected(
                        message.channel.server
                        ):
                    pass
                else:
                    await bot.join_voice_channel(
                        message.author.voice_channel
                        )
                vc = bot.voice_client_in(
                        message.channel.server
                        )
                player = await vc.create_ytdl_player(
                        "https://www.youtube.com/watch?v=wqzLoXjFT34"
                        )
                player.start()
            elif isMatch(tokens[1],"bustin"):
                if bot.is_voice_connected(
                        message.channel.server
                        ):
                    pass
                else:
                    await bot.join_voice_channel(
                        message.author.voice_channel
                        )
                vc = bot.voice_client_in(
                        message.channel.server
                        )
                player = await vc.create_ytdl_player(
                        "https://www.youtube.com/watch?v=ybcS7CP4Om0"
                        )
                player.start()
            elif isMatch(tokens[1],"familiar"):
                if bot.is_voice_connected(
                        message.channel.server
                        ):
                    pass
                else:
                    await bot.join_voice_channel(
                        message.author.voice_channel
                        )
                vc = bot.voice_client_in(
                        message.channel.server
                        )
                player = await vc.create_ytdl_player(
                        "https://www.youtube.com/watch?v=H45jqrhcsOY"
                        )
                player.start()
            else:
                pass
        else:
            pass
    else:
        pass

