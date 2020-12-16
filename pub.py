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
	embedHelp=discord.Embed(title="Invite Link", url="https://discord.com/api/oauth2/authorize?client_id=764164847238643774&permissions=8&scope=bot", color=0xf90101)
	embedHelp.set_author(name="Rednek's Bot", url="https://rednek46.github.io", icon_url="https://cdn.discordapp.com/attachments/764604032861732874/774652841276735508/ico.gif")
	embedHelp.add_field(name="Contribute to this project", value="Join [Galactic Empire](https://discord.gg/2URJ9HF)", inline=False)
	embedHelp.add_field(name="Also Fill this form to for selection", value="[Google Form](https://forms.gle/HrqAgYsM2Jhz3qZv6)", inline=False)
	embedHelp.set_footer(text="Currently WIP and subjected for a huge change.")
	await ctx.send(embed=embedHelp)
	embedPublish=discord.Embed(title="Auto Publish",color=0xf90101)
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