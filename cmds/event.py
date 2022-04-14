import discord
from discord.ext import commands
from core.classes import Cog_Evtension
import json
import random
with open('setting.json',mode ='r',encoding ='utf8') as jFile:
    jdata = json.load(jFile)

class Event(Cog_Evtension):
    
    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author == self.bot.user:
            return

        words =['海','嗨']
        if any(word in message.content.lower() for word in words):
             ans = random.choice(jdata["answer"])
             await message.channel.send(ans)

    
def setup(bot):
    bot.add_cog(Event(bot))