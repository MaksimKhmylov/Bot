from pyrogram.types import KeyboardButton
from pyrogram import emoji

back_button = KeyboardButton(f"{emoji.BACK_ARROW}Back")

time_button = KeyboardButton(f"{emoji.TIMER_CLOCK}Time")
date_button = KeyboardButton(f"{emoji.CALENDAR}Date")
help_button = KeyboardButton(f"{emoji.TAG_QUESTION_MARK}Help")