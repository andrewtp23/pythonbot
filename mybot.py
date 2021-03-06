import discord
import asyncio
import json
from cleverbot import Cleverbot

client = discord.Client()
cb = Cleverbot('bot')

with open('mybot.json') as json_data:
     d = json.load(json_data)
	 
@client.event
async def on_ready():
    print("I'm ready.")

@client.event
async def on_message(message):
   if not message.author.bot:   
        if message.content.startswith('!test'):
           counter = 0
           tmp = await client.send_message(message.channel, 'Calculating messages...')
           async for log in client.logs_from(message.channel, limit=100):
              if log.author == message.author:
                 counter += 1

              await client.edit_message(tmp, 'You have {} messages.'.format(counter))
		
        if message.content.startswith('!sleep'):
            await asyncio.sleep(5)
            await client.send_message(message.channel, 'Done sleeping')

        if client.user in message.mentions:
            await client.send_message(message.channel, cb.ask(message.content) )	
		
        if d[message.content]:
            await client.send_message(message.channel, d[message.content])

        
client.run('x')
