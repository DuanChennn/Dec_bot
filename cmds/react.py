import discord
from discord.ext import commands
from core.classes import Cog_Evtension
import json
import random
with open('setting.json',mode ='r',encoding ='utf8') as jFile:
    jdata = json.load(jFile)
   
class React(Cog_Evtension):
     @commands.command()
     async def joke(self,ctx):
        random_joke = random.choice(jdata['joke'])
        await ctx.send(random_joke)

     @commands.command()
     async def askImage(self,ctx):
        random_pic = random.choice(jdata['pic'])
        pic = discord.File(random_pic)
        await ctx.send(file = pic)

     @commands.command()
     async def web(self,ctx):
        pic = random.choice(jdata['url_pic'])
        await ctx.send(pic)

     @commands.command()
     async def bingo(self,ctx):
        pic = random.choice(jdata['bingo'])
        response = 'here you are..'+ pic
        await ctx.reply(response)
        #await ctx.send(pic)
        



def setup(bot):
    bot.add_cog(React(bot))