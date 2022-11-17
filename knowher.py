import discord
import string
from key import BOT_KEY

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    words = message.content.split()
    for word in words:

        # Strips string of punctuation
        word = word.translate(str.maketrans('', '', string.punctuation))

        if word.endswith('er'):

            # Doesn't trigger the message if the word is just 'her'
            if word == 'her':
                return

            # Sends the joke message    
            text = word.capitalize() + "? I hardly even know her!"
            await message.channel.send(text)

client.run(BOT_KEY)
