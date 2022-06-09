#!/usr/bin/env python
#
# Copyright (C) 2021 Ashwin DS <astroashwin@outlook.com>
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation;
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, see <http://www.gnu.org/licenses/>.

import os
import random
import time
from telegram import *
from telegram.ext import *
import requests
import json
import texts, info

BOT_API = os.environ.get("BOT_API")

bot = Bot(BOT_API)
updater = Updater(BOT_API, use_context=True, workers=128)
dispatcher = updater.dispatcher
timeout = 60

def trigger_fun(update: Update, context: CallbackContext):
    supported_devices = []

    in_official_devices_list = False
    in_releases_devices_list = False

    request = requests.get("https://raw.githubusercontent.com/PixelOS-Pixelish/official_devices/twelve/API/devices.json")
    json_processed = json.loads(request.content)

    for devices in json_processed:
        if devices['active'] and devices["codename"] == update.message.text.split(" ")[1]:
            in_official_devices_list = True
            print ("Device is in Official list")
            break
    
    request = requests.get("https://raw.githubusercontent.com/PixelOS-Pixelish/official_devices/twelve/API/devices.json")
    json_processed = json.loads(request.content)

    for devices in json_processed:
        if devices['active'] and devices["codename"] == update.message.text.split(" ")[1]:
            in_official_devices_list = True
            print ("Device is in Official list")
            break



    message = "The following devices have Official Project Sakura builds:\n\n"
    number = 1
    for i in supported_devices:
        message = message + str(number) + ". " + str(i) + "\n"
        number += 1

    message_sent = bot.send_message(disable_web_page_preview=True, parse_mode="HTML", chat_id=update.effective_chat.id,
                                    text=message, reply_to_message_id=update.message.message_id, )

    auto_delete(message_sent, update)


trigger_command = CommandHandler("trigger", trigger_fun, run_async=True)

dispatcher.add_handler(trigger_command)

updater.start_polling()