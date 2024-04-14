import discord
from discord import Intents
from my_api import get_random_duck, get_weather
from translate import translate
from auth import TOKEN


intents = Intents.default()
intents.messages = True
intents.reactions = True
intents.message_content = True
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print('Зашел как', client.user)

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    # !weather lon 73.0 lat 49.8
    if '!translate' in message.content:
        text = ' '.join(message.content.split()[1:])
        await message.channel.send('Ожидайте перевод...')
        res = translate(text)
        await message.channel.send(res)
    if 'lon' in message.content and 'lat' in message.content and '!weather':
        _, _, lon, _, lat = message.content.split()
        res = get_weather(lon, lat) 
        await message.channel.send('время | облачность | температура | осадки\n' + res)
    if message.content == '!duck':
        url = get_random_duck()
        await message.channel.send(url)
    if message.content == 'hello':
        await message.channel.send('Hello, World!')
        
client.run(TOKEN)