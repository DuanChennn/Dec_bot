import datetime
import discord
from discord.ext import commands
from core.classes import Cog_Evtension

class Main(Cog_Evtension):
    @commands.command()
    async def botLatency(self,ctx):
       await ctx.send(f'{round(self.bot.latency*1000)}(ms)')
       
    @commands.command()
    async def profile(self,ctx):
        embed=discord.Embed(title="onitama future teller", url="https://game.onitama.io/", description="Im #1 in onitama", color=0xd43535, timestamp = datetime.datetime.now())
        embed.set_author(name="teller", url="https://game.onitama.io/", icon_url="https://picsum.photos/50")
        embed.set_thumbnail(url="https://picsum.photos/100")
        embed.add_field(name="1", value="1", inline=True)
        embed.add_field(name="d", value="11", inline=True)
        embed.add_field(name="a", value="22", inline=True)
        embed.add_field(name="d", value="22", inline=True)
        embed.set_footer(text="footer")
        await ctx.send(embed=embed)

    #@commands.command()
    #async def whoAmI(self,ctx):
        #await ctx.send(ctx.author)
        #print(datetime.datetime.now().strftime("%H%M"))

    @commands.command()
    async def repeat(self,ctx,*,msg):
        await ctx.message.delete()
        await ctx.send(msg)

    @commands.command()
    async def purge(self,ctx,num: int):
        await ctx.channel.purge(limit=num+1)
        

def setup(bot):
    bot.add_cog(Main(bot))