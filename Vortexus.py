import discord
from discord.ext import commands

TOKEN='TOKEN HERE'

client = commands.Bot(command_prefix="?")

@client.event
async def on_ready():
  print('Connected')

@client.event 
async def on_message(message):
    if message.content == "ping":
      await client.send_message(message.channel, "pong!")
      await client.add_reaction(message, '\N{THUMBS UP SIGN}')
    if message.content == "help":
      emb = (discord.Embed(description="Commands can be found [here](https://github.com/Infinixius/vortexus/wiki/Commands)", colour=0x3DF270))
      emb.set_author(name="Commands")
      await client.send_message(message.channel, embed=emb)
    if message.content == "about":
      emb = (discord.Embed(description="Vortexus is a bot maintained by [Infinixius](https://infinixius.co.nf), this is a port of Vortexus in discord.py by mayojar#7199. Run ?cmds for help. You are running version 1.4.0.0-beta", colour=0x3DF270))
      emb.set_author(name="About")
      await client.send_message(message.channel, embed=emb)


      



client.run(TOKEN)

