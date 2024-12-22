import datetime
import random

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


@bot.on_message(filters.command("time"))
async def echo(client: Client, message):
    await message.reply(datetime.datetime.now().strftime("%I:%M:%S %p"))

@bot.on_message(filters.command("date"))
async def echo(client: Client, message):
    await message.reply(datetime.date.today())

@bot.on_message(filters.text)
async def echo(client: Client, message):
    await message.reply(random_text(message.text))

bot.run()
