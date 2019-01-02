import discord
from discord.ext import commands

TOKEN='TOKEN HERE'

bot = commands.Bot(command_prefix = "!")

@bot.event
async def on_ready():
  print('Connected')

@bot.event 
async def on_message(message):
    if message.content == "!ping":
      await bot.send_message(message.channel, "pong!")
      await bot.add_reaction(message, '\N{THUMBS UP SIGN}')
    if message.content == "!help":
      emb = (discord.Embed(description="Commands can be found [here](https://github.com/majormayojar/Vortexus-Python/wiki/Commands)", colour=0x3DF270))
      emb.set_author(name="Commands")
      await bot.send_message(message.channel, embed=emb)
    if message.content == "!about":
      emb = (discord.Embed(description="Vortexus is a bot maintained by [Infinixius](https://infinixius.co.nf), this is a port of Vortexus in discord.py by [mayojar](mayojar.co.nf). Run ?cmds for help. You are running version 1.4.0.0-beta", colour=0x3DF270))
      emb.set_author(name="About")
      await bot.send_message(message.channel, embed=emb)
    if message.content == "!debug test":
      print("Test")
      await bot.add_reaction(message, '\N{THUMBS UP SIGN}')
    if message.content == "!debug end":
      await bot.close()

      


bot.run(TOKEN)

