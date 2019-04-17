# --------- std/extra libraries
import requests
import time
import os
import urllib

from sqlite3 import Error
# -------- project modules
from bot.utils import is_available_command, command_takes_arguments, get_hint_message, get_command_handler
from bot.db import DBHelper
from bot.data_types import User, Message

bot_token = os.environ.get("BOT_TOKEN")
if not bot_token:
    exit("Provide your telegram bot token!")
# base url for our requests to the telegram APIs
URL = f"https://api.telegram.org/bot{bot_token}/"


def get_updates(offset=None):
    """Get updates after the offset"""
    # timeout will keep the pipe open and tell us when there"re new updates
    url = URL + f"getUpdates?timeout=120&allowed_updates={['messages']}"
    if offset:
        url += f"&offset={offset}"  # add offset if exists
    return requests.get(url).json()  # return dict of latest updates


def send_message(chat_id, text):
    """Encodes ``text`` using url-based encoding and send it to ``chat_id``"""
    requests.get(URL + f"sendMessage?chat_id={chat_id}&text={urllib.parse.quote_plus(text)}")


def last_update_id(updates):
    """takes dict of updates and return the id of last one"""
    update_ids = []
    for update in updates["result"]:
        update_ids.append(int(update["update_id"]))
    return max(update_ids)  # the last update is the higher one


# TODO:
# extract user info from update #XXX
# extract message info from update #XXX
# store message in db #XXX
# if message exists, skip
# REFACTOR DUPLICATED DATA
# check user in db
# # if exists:
# get user's last command
# current_command = user.last_command
# reply to user's message based on his/her incoming message
# update user's last_command according the incoming message
# # if not:
# add user to db
# set current command
# reply to users message based on its content
user = None
current_command = None  # stores currently operating command


def handle_updates(updates: list, db: DBHelper):
    """Handles incoming updates to the bot"""
    global current_command  # use current_command var from global scope
    for update in updates:  # loop through updates
        # db.add_message((id: int, update_id: int, user_id: int, chat_id: int, date: int(unix_timestamp), text: str))

        # TODO: common message and user data from the same update

        # getting message data
        msg_id = update["message"]["message_id"]  # message id
        msg_update_id = update["update_id"]  # update id of this message
        msg_user_id = update["message"]["from"]["id"]  # sending user
        msg_chat_id = update["message"]["chat"]["id"]  # chat id of the message
        msg_date = update["message"]["date"]  # message date
        msg_text = update["message"]["text"]  # message text

        # Create Message object from incoming data
        msg = Message(msg_id, msg_update_id, msg_user_id, msg_chat_id, msg_date, msg_text)
        if not db.get_message(msg.id):  # if message doesn't exist already
            db.add_message((msg.id, msg.update_id, msg.user_id, msg.chat_id, msg.date, msg.text))
            print("New message saved.")

        # TODO: user data
        # db.add_user((id: int, is_bot: int, is_admin: int, first_name: str, last_name: str,
        # username: str, language_code: str, active: int(0|1), created: int(unix_timestamp),
        # updated: int(unix_timestamp), last_command: str))
        user_id = update["message"]["from"]["id"]
        user_is_bot = update["message"]["from"]["is_bot"]
        user_is_admin = 0
        user_first_name = update["message"]["from"]["first_name"]
        user_last_name = update["message"]["from"]["last_name"]
        user_username = update["message"]["from"]["username"]
        user_language_code = update["message"]["from"]["language_code"]
        user_active = 1
        user_created = time.time()
        user_updated = time.time()
        user_last_command = None

        # Create user object from incoming data
        user = User(user_id, user_is_bot, user_is_admin, user_first_name, user_last_name, user_username,
                    user_language_code, user_active, user_created, user_updated, user_last_command)

        if not db.get_user(user.id):
            db.add_user(
                (user.id, user.is_bot, user.is_admin, user.first_name, user.last_name,
                    user.username, user.language_code, user.active, user.created, user.updated, user.last_command))
            print("New user saved.")

        text = None  # msg text
        chat = update["message"]["chat"]["id"]  # chat id
        if "text" in update["message"]:  # handle text messages only
            text = update["message"]["text"].strip()  # extract msg text
            if text and chat:  # make sure we have txt msg and chat_id
                if text.startswith("/"):  # if command
                    if is_available_command(text):  # if command is available
                        current_command = text  # set current command
                        if command_takes_arguments(current_command):  # if command operates on arg
                            hint_message = get_hint_message(current_command)  # get command hint message
                            send_message(chat, hint_message)  # send a help message to receive argument
                        else:  # if command is available and does not operate on arg
                            # execute command directly
                            send_message(chat, get_command_handler(current_command)())
                            # then unset current_command, commands_without_args execute once!
                            current_command = None
                    else:  # if command is not available
                        send_message(chat, "Use a defined command.")
                else:  # if sent message does not start with a slash
                    if current_command:  # should be an argument if current_command is set
                        current_command_service = get_command_handler(current_command)  # get se
                        send_message(chat, current_command_service(text))
                    else:
                        send_message(chat, "Use a defined command.")
        else:  # if no text message
            send_message(chat, "I handle text messages only!")


def main(db: DBHelper):
    """The entry point"""
    updates_offset = None  # track last_update_id to use it as offset
    while True:  # infinitely listen to new updates (as long as the script is running)
        try:
            print("getting updates...")
            updates = get_updates(updates_offset)  # get new updates after last handled one
            if "result" in updates:  # to prevent KeyError exception
                if len(updates["result"]) > 0:  # make sure updates list is longer than 0
                    updates_offset = last_update_id(updates) + 1  # to remove handled updates
                    handle_updates(updates["result"], db)  # handle new (unhandled) updates
            time.sleep(0.5)
        except KeyboardInterrupt:  # exit on Ctrl-C
            print("\nquiting...")
            exit(0)


if __name__ == "__main__":
    # Setting DB
    db = DBHelper()
    db.setup()
    print("Running bot...")
    main(db)
