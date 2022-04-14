import discord
from discord.ext import commands
from core.classes import Cog_Evtension
import json
import random
with open('setting.json',mode ='r',encoding ='utf8') as jFile:
    jdata = json.load(jFile)

class Event(Cog_Evtension):
    @commands.Cog.listener()
    async def on_member_join(self, member):
     channel = self.bot.get_channel(int(jdata['channel_lobby']))
     await channel.send(f'{member} join')

    @commands.Cog.listener()
    async def on_member_remove(self, member):
     print(f'{member} left!')
     channel = self.bot.get_channel(int(jdata['channel_lobby']))
     await channel.send(f'{member} leave')

    @commands.Cog.listener()
    async def on_message(self, message):
        words =['海','嗨']
        if any(word in message.content.lower() for word in words) and message.author!= self.bot.user:
             ans = random.choice(jdata["answer"])
             await message.channel.send(ans)
        else:
             await self.bot.process_commands(message)
    


     

def setup(bot):
    bot.add_cog(Event(bot))