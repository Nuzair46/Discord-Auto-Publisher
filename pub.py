import discord
import os
from discord.ext import commands
from collections import deque

## Bot to publish announcements

client = commands.Bot(command_prefix = 'r!')
client.remove_command("help")


creds = open('token.txt', 'r')   
channelQue = deque([])

bot = commands.Bot(...)
bot.channel_id = 0

@client.event
async def on_ready():
	await client.change_presence(status = discord.Status.dnd, activity = discord.Game('r!help'))
	print('Ready..')


@client.command(pass_context=True)
async def set(ctx, arg):
	bot.channel_id = arg[2:-1]
	channel = client.get_channel(int(bot.channel_id))
	await ctx.send(f"Set to Publish channel {bot.channel_id}")
	channelQue.append(int(bot.channel_id))


@client.command()
async def help(ctx):
	embedPublish=discord.Embed(title="Auto Publisher",color=0xf90101)
	embedPublish.add_field(name="Usage", value="r!set #channelname", inline=False)
	await ctx.send(embed=embedPublish)

@client.event
async def on_message(message):
	await client.process_commands(message)
	for channel in channelQue:
		if channel == message.channel.id:
			await message.publish()

## Don't edit under this line.
key = creds
client.run(key.read())