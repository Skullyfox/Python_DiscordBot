import discord
from functions import OnMessage

def Auth(Token):
    class MyClient(discord.Client):
        async def on_ready(self):
            print('Logged on as', self.user)

        async def on_message(self, message):
            splittedMessage = message.content.split(' ')
            
            # don't respond to ourselves
            if message.author == self.user:
                return

            if message.content == 'ping':
                await OnMessage.pong(message)
            
            if splittedMessage[0] == '!embed':
                await OnMessage.embed(message)


    client = MyClient()
    client.run(Token)