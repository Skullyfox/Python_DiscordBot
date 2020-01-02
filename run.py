import discord
from discord.ext import commands
from dotenv import dotenv_values
import functions

TOKEN = dotenv_values().get('TOKEN')

functions.Auth(TOKEN)