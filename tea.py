# --------- libraries
import requests
import time
import sys
import os
import urllib

# --------- project modules
# --------- commands
from tbot.commands import start_command
from tbot.commands import help_command
from tbot.commands import weather
from tbot.commands import translate
from tbot.commands import calculate
from tbot.commands import tweet
from tbot.commands import ocr_url
# from tbot.commands import ocr_file

bot_token = os.environ.get("BOT_TOKEN")
if not bot_token:
    sys.stderr.write("Provide your telegram bot token!")
    sys.exit(1)
# base url for our requests to the telegram APIs
URL = f"https://api.telegram.org/bot{bot_token}/"


def dict_from_url(url):
    """return json response in form of python dictionary"""
    return requests.get(url).json()  # return the result as a python dictionary


def get_updates(offset=None):
    """Get updates after the offset"""
    # timeout will keep the pipe open and tell us when there"re new updates
    url = URL + f"getUpdates?timeout=120&allowed_updates={['messages']}"
    if offset:
        url += f"&offset={offset}"  # add offset if exists
    return dict_from_url(url)  # return dict of latest updates


def send_message(chat_id, text):
    """Encodes ``text`` using url-based encoding and send it to ``chat_id``"""
    requests.get(URL + f"sendMessage?chat_id={chat_id}&text={urllib.parse.quote_plus(text)}")


def last_update_id(updates):
    """takes dict of updates and return the id of last one"""
    update_ids = []
    for update in updates["result"]:
        update_ids.append(int(update["update_id"]))
    return max(update_ids)  # the last update is the higher one


current_command = None  # stores currently operating command


def is_available_command(command):
    """Checks if ``command`` is available in TBot commands"""
    available_commands = ["/start", "/help", "/weather", "/translate", "/calculate", "/tweet", "/ocr_url"]
    if command in available_commands:
        return True
    return False


def command_takes_arguments(command):
    """Checks if ``command`` operates on arguments or not"""
    commands_with_argument = ["/translate", "/calculate", "/tweet", "/ocr_url"]
    if command in commands_with_argument:
        return True
    return False


def get_hint_message(command):
    """Returns a hint message of ``command``"""
    commands_hint = {
        "/start": "",
        "/help": "",
        "/weather": "",
        "/translate": "I will translate your next message from english to arabic",
        "/calculate": "Write a mathematical expression to calculate",
        "/tweet": "Let's tweet on TBot's twitter account!",
        "/ocr_url":   "Send the URL of the image you want to extract text from"
    }
    return commands_hint.get(command)


def get_command_handler(command):
    """Returns a callable function according to ``command``"""
    command_service = {
        "/start": start_command,
        "/help": help_command,
        "/weather": weather,
        "/translate": translate,
        "/calculate": calculate,
        "/tweet": tweet,
        "/ocr_url": ocr_url
    }
    return command_service.get(command)


def handle_updates(updates):
    """Handles incoming updates to the bot"""
    global current_command  # use current_command var from global scope
    for update in updates["result"]:  # loop through updates
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
                            send_message(chat, hint_message)  # send a help message to recieve argument
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


def main():
    """The entry point"""
    updates_offset = None  # track last_update_id to use it as offset
    while True:  # infinitely listen to new updates (as long as the script is running)
        try:
            print("getting updates...")
            updates = get_updates(updates_offset)  # get new updates after last handled one
            if "result" in updates:  # to prevent KeyError exception
                if len(updates["result"]) > 0:  # make sure updates list is longer than 0
                    updates_offset = last_update_id(updates) + 1  # to remove handled updates
                    handle_updates(updates)  # handle new (unhandled) updates
            time.sleep(0.5)
        except KeyboardInterrupt:  # exit on Ctrl-C
            print("\nquiting...")
            sys.exit(0)


if __name__ == "__main__":
    main()
