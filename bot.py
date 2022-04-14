import discord
from discord.ext import commands
import json
import os

with open('setting.json',mode ='r',encoding ='utf8') as jFile:
    jdata = json.load(jFile)

bot  = commands.Bot(command_prefix = '[')

@bot.event
async def on_ready():
    print(">>Im here<<")


@bot.command()
async def load(ctx, extendsion):
    bot.load_extension(f'cmds.{extendsion}')
    await ctx.send(f'loaded {extendsion} done.')

@bot.command()
async def unload(ctx, extendsion):
    bot.unload_extension(f'cmds.{extendsion}')
    await ctx.send(f'unloaded {extendsion} done.')

@bot.command()
async def reload(ctx, extendsion):
    bot.reload_extension(f'cmds.{extendsion}')
    await ctx.send(f'reloaded {extendsion} done.')


for filename in os.listdir('./cmds'):
    if filename.endswith('.py'):
        bot.load_extension(f'cmds.{filename[:-3]}')
        print(filename)



bot.run(jdata['token'])
