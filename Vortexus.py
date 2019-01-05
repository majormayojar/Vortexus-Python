import discord
import asyncio
from discord.ext import commands

TOKEN='TOKEN HERE'

bot = commands.Bot(command_prefix="!")

chat_filter = ["PINAPPLE","APPLE", "CHROME"] 
bypass_list = ["userid"] 

@bot.event
async def on_ready():
  print('Connected')
  await bot.change_presence(game=discord.Game(name='!help for help'))

@bot.event
async def on_member_join():
  rolee = discord.utils.get(server.roles, name='rolename here')
  await bot.add_roles(member.server.roles, rolee)

@bot.command(pass_context=True)
async def kick(ctx, member: discord.Member = None):
    if not member:
        return await bot.say("Specify a member please")
    else:
      await bot.kick(member)

@bot.command(pass_context=True)
async def ban(ctx, member: discord.Member = None):
    if not member:
        return await bot.say("Specify a member please")
    await bot.ban(member)

@bot.command(pass_context=True)
async def mute(ctx, member: discord.Member=None):
    if not member:
        return await bot.say("Specify a member please")
    role = discord.utils.get(ctx.message.server.roles, name="muted")
    await bot.add_roles(member, role)

@bot.command(pass_context=True)
async def unmute(ctx, member: discord.Member=None):
    if not member:
        return await bot.say("Specify a member please")
    role = discord.utils.get(ctx.message.server.roles, name="muted")
    await bot.remove_roles(member, role)

@bot.event 
async def on_message(message):
    contents = message.content.split(" ")
    for word  in contents:
      if word.upper() in chat_filter:
        if not message.author.id in bypass_list:
          await bot.delete_message(message)
          await bot.send_message(message.channel, "**Hey!** You can't use that word")
        

   
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
      if message.author.id == "userid":
        print("Test")
        await bot.add_reaction(message, '\N{THUMBS UP SIGN}')
      else:
        await bot.add_reaction(message, '\N{NO ENTRY}')
        await bot.send_message(message.channel, "Sorry, Only the owner can use that command.")
    if message.content == "!debug end":     
      if message.author.id == "userid":
        await bot.close()
        print("Powering off")
      else:
        await bot.send_message(message.channel, "You cannot use this command")
        await bot.add_reaction(message, '\N{NO ENTRY}')
    await bot.process_commands(message)



bot.run(TOKEN)

