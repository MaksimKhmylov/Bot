import datetime
import random

from pyrogram.filters import reply_keyboard

import keyboards

from pyrogram import Client, filters

import config

bot = Client(
    api_id=config.API_ID,
    api_hash=config.API_HASH,
    bot_token=config.AUTH_TOKEN,
    name="my_cool_bot",
)

def random_text(text):
    text = list(text)
    return "".join(sorted(text, key=lambda sort: random.random()))


@bot.on_message(filters.command("start"))
async def echo(client: Client, message):
    await message.reply('hello', reply_markup = keyboards.main_keyboard)


@bot.on_message(filters.command("help") | filters.regex(r"^.Help"))
async def echo(client: Client, message):
    await message.reply("""commands: \n
    /time - time\n
    /date - date\n
    /help - help\n
    """)

@bot.on_message(filters.command("time") | filters.regex(r"Time"))
async def echo(client: Client, message):
    await message.reply(datetime.datetime.now().strftime("%I:%M:%S %p"))

@bot.on_message(filters.command("date") | filters.regex(r"^.Date"))
async def echo(client: Client, message):
    await message.reply(datetime.date.today())

@bot.on_message(filters.text)
async def echo(client: Client, message):
    await message.reply(random_text(message.text))

bot.run()
