import requests
from telegram import Update
from telegram.ext import CallbackContext

from FallenRobot import dispatcher
from FallenRobot.modules.disable import DisableAbleCommandHandler


def truth(update: Update, context: CallbackContext):
    truth = requests.get(f"https://api.truthordarebot.xyz/v1/truth").json()["question"]
    update.effective_message.reply_text(truth)


def dare(update: Update, context: CallbackContext):
    dare = requests.get(f"https://api.truthordarebot.xyz/v1/dare").json()["question"]
    update.effective_message.reply_text(dare)


TRUTH_HANDLER = DisableAbleCommandHandler("truth", truth, run_async=True)
DARE_HANDLER = DisableAbleCommandHandler("dare", dare, run_async=True)

dispatcher.add_handler(TRUTH_HANDLER)
dispatcher.add_handler(DARE_HANDLER)


__help__ = """
*Həqiqət və Cəsarət*

 ❍ /truth *:* Təsadüfi həqiqət sətrini göndərir.
 ❍ /dare *:* Təsadüfi cəsarətli simli göndərir.
"""

__mod_name__ = "Tʀᴜᴛʜ-Dᴀʀᴇ"
