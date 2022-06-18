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

BOT_API = os.environ.get("BOT_API")

bot = Bot(BOT_API)
updater = Updater(BOT_API, use_context=True, workers=128)
dispatcher = updater.dispatcher
timeout = 60

admins = [
    "1366397711", "1054531133", "966374317", "771065537", "336444854", "2122096311", "964564403", "1389936430",
]

def trigger_fun(update: Update, context: CallbackContext):
    supported_devices = []

    in_official_devices_list = False

    request = requests.get("https://raw.githubusercontent.com/PixelOS-Pixelish/official_devices/twelve/API/devices.json")
    json_processed = json.loads(request.content)
    for devices in json_processed["devices"]:
        current_device = update.message.text.split(" ")[1]
        current_device = current_device.replace(" ", "")
        print (current_device)
        print (devices)
        if devices["codename"] == current_device:
            in_official_devices_list = True
            print ("Device is in Official list")
            break
    
    if str(update.message.from_user.id) in admins and not in_official_devices_list:
        bot.send_message(disable_web_page_preview=True, parse_mode="HTML", chat_id=update.effective_chat.id,
                                    text="Device not found in official devices list\nAdd it to https://github.com/PixelOS-Pixelish/official_devices/blob/twelve/API/devices.json", reply_to_message_id=update.message.message_id, )

    if str(update.message.from_user.id) in admins and in_official_devices_list:
        os.system("cd releases && echo $(pwd) && gh workflow run " + update.message.text.split(" ")[1] + "-s.yml")

        message_to_send = "Build for " + current_device + " has been triggered"

        message_sent = bot.send_message(disable_web_page_preview=True, parse_mode="HTML", chat_id=update.effective_chat.id,
                                    text=message_to_send, reply_to_message_id=update.message.message_id, )



trigger_command = CommandHandler("trigger", trigger_fun, run_async=True)

dispatcher.add_handler(trigger_command)

updater.start_polling()
