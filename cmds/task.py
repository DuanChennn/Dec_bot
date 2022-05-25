import discord
from discord.ext import commands
from core.classes import Cog_Evtension
import json,asyncio,datetime
import random
with open('setting.json',mode ='r',encoding ='utf8') as jFile:
    jdata = json.load(jFile)

class Task(Cog_Evtension):
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        
        self.countrer = 0
        # async def interval():
        #     await self.bot.wait_until_ready()
        #     self.channel = self.bot.get_channel(int(jdata["channel_test"]))
        #     while not self.bot.is_closed():
        #         random_ans = random.choice(jdata["auto_ans"])
        #         await self.channel.send(random_ans)
        #         await asyncio.sleep(180)#單位秒
        # self.bg_task = self.bot.loop.create_task(interval())

        # async def gabbageTruck():
        #     await self.bot.wait_until_ready()
        #     self.channel = self.bot.get_channel(int(jdata["channel_test"]))
        #     while not self.bot.is_closed():
        #         await self.channel.purge(limit=5)
        #         await asyncio.sleep(1800)#單位秒
        # self.bg_task = self.bot.loop.create_task(gabbageTruck())

        async def time_task():
            await self.bot.wait_until_ready()
            self.channel = self.bot.get_channel(int(jdata["channel_test"]))
            while not self.bot.is_closed():
                now_time = datetime.datetime.now().strftime("%H%M")
                if(now_time == jdata["alarm_time"] and self.countrer == 0):
                    await self.channel.send('Go')
                    self.countrer = 1
                    await asyncio.sleep(1)
                else:
                    await asyncio.sleep(1)
                    pass
        self.bg_task = self.bot.loop.create_task(time_task())

        

    @commands.command()
    async def set_channel(self,ctx,ch: int):
        self.channel = self.bot.get_channel(ch)
        await ctx.send(f'Set Channel: {self.channel.mention}')
    
    @commands.command()
    async def set_alarm(self,ctx,time):
        self.countrer = 0
        jdata['alarm_time'] = time
        with open('setting.json','w',encoding ='utf8') as jwfile:
            json.dump(jdata,jwfile, indent =4)

        

        

def setup(bot):
    bot.add_cog(Task(bot))