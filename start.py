import os
import discord
from discord.ext import commands
from src.structs.Client import Client
from src.utils.logger import get_logger
from src.utils.PostgresHelper import PostgresHelper

# Load environment variables
from dotenv import load_dotenv
load_dotenv()

TOKEN = os.getenv('TOKEN')
PREFIX = os.getenv('PREFIX')
PG_HOST = os.getenv('PG_HOST')
PG_NAME = os.getenv('PG_NAME')
PG_USER = os.getenv('PG_USER')
PG_PASS = os.getenv('PG_PASS')
PG_PORT = os.getenv('PG_PORT')

# Initialize logger
logger = get_logger()

# Initialize PostgreSQL helper
db_helper = PostgresHelper(user=PG_USER, password=PG_PASS, host=PG_HOST, port=PG_PORT, database=PG_NAME)

# Initialize bot
intents = discord.Intents.default()
intents.messages = True
intents.guilds = True
bot = Client(command_prefix=PREFIX, intents=intents)

# Load cogs
initial_extensions = [
    'src.commands.admin.lang',
    'src.commands.admin.prefix',
    'src.commands.admin.sAdmin',
    'src.commands.c',
    'src.commands.corp',
    'src.commands.h',
    'src.commands.handle',
    'src.commands.referral',
    'src.commands.s',
    'src.commands.scstats',
    'src.commands.stats',
    'src.events.guildCreate',
    'src.events.message'
]

if __name__ == '__main__':
    for extension in initial_extensions:
        bot.load_extension(extension)

# Start bot
bot.run(TOKEN)
