import discord

async def pong(message):
    await message.channel.send('pong')

async def embed(message):

    embedMessage = discord.Embed(title="🚀 Test d'embed 🚀", description="Ceci est un test d'embed réalisé par un bot développé en Python", color=0x34bcef)
    # embedMessage.add_field(name=field.name, value=field.value, inline=False)
    await message.channel.send(embed = embedMessage)
    await message.delete()

    

