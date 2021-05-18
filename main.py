import discord
from discord.ext import commands
import os
import random
from keep_alive import keep_alive

client =commands.Bot(command_prefix = '$',)
@client.event
async def on_ready():
  await client.change_presence(status=discord.Status.online, activity=discord.Game('$Help for Help'))
  print('Bot is ready.')



#Provides Help
@client.command(pass_context=True)
async def Help(ctx):
  
  embed = discord.Embed(
    title='Help From Utility',
    description='These are Commands followed by $',
    colour= discord.Colour.blue()
  )
  embed.set_author(name="Made By RADIUMz", 
  url="https://www.instagram.com/mr._kaamchor/", 
  #icon_url="https://drive.google.com/file/d/1gD34uocVAzkBd24Eiika3qbTvBotIEfc/view?usp=sharing"
  )
  embed.add_field(name="1)  ping", value="gives response ping from server", inline=False)
  embed.add_field(name="2)  ask, answer, guess", value="randomly guesses your fate", inline=False)
  embed.add_field(name="3)  clean, delete, purge, clear", value="helps clear trash messages", inline=False)
  embed.add_field(name="4)  roll, dice", value="your virtual dice at your command", inline=False)
  embed.add_field(name="5)  toss", value="returns HEADS or TAILS", inline=False)
  embed.set_footer(text='Hope it helps. Cheers!')
  
  await ctx.send(embed=embed)

  


#gives response ping
@client.command()
async def ping(ctx):
  await ctx.send(f'Ping = {round(client.latency* 1000)}ms')


#random fate guesser
@client.command(aliases=['answer','guess'])
async def ask(ctx, *, question):
    response = ['It is certain.',
    'It is decidedly so.',
    'Without a doubt.',
    'Yes – definitely.',
    'You may rely on it.',
    'As I see it, yes.',
    'Most likely.',
    'Outlook good.',
    'Yes.',
    'Signs point to yes.',
    'Reply hazy, try again.',
    'Ask again later.',
    'Better not tell you now.',
    'Cannot predict now.',
    ' Concentrate and ask again.',
    'Dont count on it.',
    ' My reply is no.',
    'My sources say no.',
    'Outlook not so good.',
    'Very doubtful.']

    await ctx.send(f'Question : {question}\nAnswer: {random.choice(response)}')

#Clear Messages
@client.command(aliases=['clean','purge','delete'])
async def clear(ctx, amount=10):
    await ctx.channel.purge(limit=amount+1)
    await ctx.send(f'Messages Cleared')

#Roll the Dice
@client.command(aliases=['dice'])
async def roll(ctx):
    response=['1', '2', '3', '4', '5', '6']
    await ctx.send(f'{random.choice(response)}')

#Toss a Coin
@client.command()
async def toss(ctx):
    response=['HEADS','TAILS']
    await ctx.send(f'{random.choice(response)}')


keep_alive()
client.run(os.getenv("TOKEN"))