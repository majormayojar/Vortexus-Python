import discord
from discord.ext import commands

TOKEN='TOKEN HERE'

bot = commands.Bot(command_prefix = "!")

chat_filter = ["PINAPPLE","APPLE", "CHROME"] #put your whitelisted words in the quotations
bypass_list = ["userid"] #put a userid for people that can say the whitelisted words here

@bot.event
async def on_ready():
  print('Connected')
  await bot.change_presence(game=discord.Game(name='!help for help'))

@bot.event 
async def on_message(message):
    contents = message.content.split(" ")
    for word  in contents:
      if word.upper() in chat_filter:
        if not message.author.id in bypass_list:
          await bot.delete_message(message channel, "**Hey!** You can't use that word")
          await bot.send_message(message.)
   
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
      await bot.change_presence(game=discord.Game(name='Powering off'))

      


bot.run(TOKEN)

