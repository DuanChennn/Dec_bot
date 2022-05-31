import discord
from discord.ext import commands
from core.classes import Cog_Evtension
import json
import random
import os
with open('setting.json',mode ='r',encoding ='utf8') as jFile:
    jdata = json.load(jFile)

class React(Cog_Evtension):
     @commands.command()
     async def joke(self,ctx):
        random_joke = random.choice(jdata['joke'])
        await ctx.send(random_joke)

     @commands.command()
     async def askImage(self,ctx):
        #random_pic = random.choice(jdata['pic'])
        #pic = discord.File(random_pic)
        pic = discord.File('/Users/duanchennn/Documents/UnityProject/Dec_bot/Images/hammer.png')
        await ctx.send(file = pic)
        #await ctx.send(file = pic)

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

      ###pick up card from local pngs  
     @commands.command()
     async def card(self,ctx):
        random_pic = random.choice(jdata['pic'])
        pic = discord.File(random_pic)
        await ctx.reply(file = pic, content ="here you are..")

      ###pick up card from url  
     @commands.command()
     async def card2(self,ctx):
        pic2 = random.choice(jdata['bingo'])
        await ctx.reply(content ="here you are.."+pic2)

     ###pick up card from url and send out with embed
     @commands.command()
     async def Card(self,ctx):
        pic = random.choice(jdata['bingo'])
        embed=discord.Embed(title="onitama future teller", url="https://game.onitama.io/", color=0xd43535)
        #embed.set_author(name="teller", url="https://game.onitama.io/", icon_url="https://picsum.photos/50")
        embed.set_thumbnail(url=pic)
        #embed.set_footer(text="now you know what should do")
        await ctx.reply(embed=embed)

      ###pick up card with relative position 
     @commands.command()
     async def GetPic(self,ctx):
        value = random.randint(1,3)
        pngName = "card{index}.png".format(index = value)
        imgPath = os.path.join(os.getcwd(),'Images',pngName)
        pic = discord.File(imgPath)
        await ctx.reply(file = pic, content ="here you are..")

     @commands.command()
     async def TestInTestChannel(self,ctx):
        #964011041925255210
        if(ctx.channel.name == 'test'):
         value = random.randint(1,2)
         pngName = "card{index}.png".format(index = value)
         imgPath = os.path.join(os.getcwd(),'Images',pngName)
         pic = discord.File(imgPath)
         await ctx.reply(file = pic, content ="here you are..")
        else:
          await ctx.reply("im in other channnel")

     @commands.command()
     async def TheAnswer(self,ctx):
        #channel_talkable
        if(ctx.channel.id == jdata['channel_talkable']):
         value = random.randint(1,11)
         pngName = "card{index}.png".format(index = value)
         imgPath = os.path.join(os.getcwd(),'Images',pngName)
         pic = discord.File(imgPath)
         await ctx.reply(file = pic, content ="here you are..")
        else:
          await ctx.reply("im in other channnel")



def setup(bot):
    bot.add_cog(React(bot))