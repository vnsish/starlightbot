import os
from twitchio.ext import commands
from config import *
from time import time
import utils

from papago import Translator
translator = Translator(PAPAGO_ID, PAPAGO_SECRET)

bot = commands.Bot(
    irc_token=TMI_TOKEN,
    client_id=CLIENT_ID,
    nick=BOT_NICK,
    prefix=BOT_PREFIX,
    initial_channels=CHANNEL
)

now = time()

@bot.event
async def event_ready():
    print(f"Bot online")

@bot.event
async def event_message(ctx):
    if ctx.author.name.lower() == BOT_NICK.lower():
        return
    await bot.handle_commands(ctx)
    #print(f'{ctx.channel} - {ctx.author.name}: {ctx.content}')

@bot.command(name='test')
async def my_command(ctx):
	await ctx.send(f'Hello {ctx.author.name}!')	

@bot.command(name='translate')
async def trans(ctx):
	global now
	if utils.elapsed(now):
		try:
			phrase = ctx.content[ctx.content.index(' ')+1:]
			print(f'translate {phrase}')
			response = utils.translate(phrase, 'en', 'ko')
			print(response)
			now = time()
			await ctx.send(f'@{ctx.author.name}, {phrase} = {response.text}')
		except ValueError:
			await ctx.send(f'@{ctx.author.name}, usage: !translate <text in english>')

@bot.command(name='translatekr')
async def trans_kr(ctx):
	global now
	if utils.elapsed(now):
		try:
			phrase = ctx.content[ctx.content.index(' ')+1:]
			print(f'translate {phrase}')
			response = utils.translate(phrase, 'ko', 'en')
			print(response)
			now = time()
			await ctx.send(f'@{ctx.author.name}, {phrase} = {response.text}')
		except ValueError:
			await ctx.send(f'@{ctx.author.name}, usage: !translatekr <text in korean>')

@bot.command(name='translatedetect')
async def trans_detect(ctx):
	global now
	if utils.elapsed(now):
		try:
			phrase = ctx.content[ctx.content.index(' ')+1:]
			lang = utils.detect_language(phrase)
			print(f'translate {phrase}')
			if lang == 'en':
				response = utils.translate(phrase, 'en', 'ko')
			elif lang == 'ko':
				response = utils.translate(phrase, 'ko', 'en')
			else:
				raise Exception('Invalid language.')

			print(response)
			now = time()
			await ctx.send(f'@{ctx.author.name}, {phrase} = {response.text}')
		except ValueError:
			await ctx.send(f'@{ctx.author.name}, usage: !translate <text>')

if __name__ == "__main__":
	bot.run()