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
  rolee = discord.utils.get(server.roles, name='RoleNameHere')
  await bot.add_roles(server.roles, rolee)

@bot.command(pass_context=True)
@commands.has_permissions(kick_members=True)
async def kick(ctx, member: discord.Member = None):
    if not member:
        return await bot.say("Specify a member please")
    else:
      await bot.kick(member)

@bot.command(pass_context=True)
@commands.has_permissions(ban_members=True)
async def ban(ctx, member: discord.Member = None):
    if not member:
        return await bot.say("Specify a member please")
    await bot.ban(member)

@bot.command(pass_context=True)
@commands.has_permissions(mute_members=True)
async def mute(ctx, member: discord.Member=None):
    if not member:
        return await bot.say("Specify a member please")
    role = discord.utils.get(ctx.message.server.roles, name="muted") #make a role called muted  
    await bot.add_roles(member, role)

@bot.command(pass_context=True)
@commands.has_permissions(mute_members=True)
async def unmute(ctx, member: discord.Member=None):
    if not member:
        return await bot.say("Specify a member please")
    role = discord.utils.get(ctx.message.server.roles, name="muted")
    await bot.remove_roles(member, role)

@bot.command(pass_context=True)
async def clear(ctx, amount=100):
  channel = ctx.message.channel
  messages = []
  async for message in bot.logs_from(channel, limit=int(amount)):
    messages.append(message)
  await bot.delete_messages(messages)
  await bot.say('Messages deleted')


@bot.command()
async def echo(*args):
  output = ''
  for word in args:
    output += word
    output += ' '
  await bot.say(output)

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
    if message.content == "!about":
      emb = (discord.Embed(description="Vortexus is a bot maintained by [Infinixius](https://infinixius.co.nf), this is a port of Vortexus in discord.py by [mayojar](mayojar.co.nf). Run ?cmds for help. You are running version 1.4.0.0-beta", colour=0x3DF270))
      emb.set_author(name="About")
      await bot.send_message(message.channel, embed=emb)
    if message.content == "!debug end":
      print("Powering Off...")
      await bot.logout()
    if message.content == "!debug test":
      print("Test")
      await bot.add_reaction(message, '\N{THUMBS UP SIGN}')  
    await bot.process_commands(message)
    


bot.run(TOKEN)

