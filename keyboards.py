from pyrogram.types import ReplyKeyboardMarkup

import paterns as b

main_keyboard = ReplyKeyboardMarkup([
    [b.date_button],
    [b.help_button, b.time_button]

])