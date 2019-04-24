"""
    Helper functions to be used inside the project
"""
from .commands import start_command, help_command, weather, translate, calculate, tweet, ocr_url, schedule, stop


def is_available_command(command):
    """Checks if ``command`` is available in TBot commands"""
    available_commands = ["/start", "/help", "/weather", "/translate", "/calculate", "/tweet", "/ocr_url", "/schedule", "/stop"]

    if command in available_commands:
        return True
    return False


def command_takes_input(command):
    """Checks if ``command`` operates on inputs or not"""
    takes_input = ["/translate", "/calculate", "/tweet", "/ocr_url"]
    if command in takes_input:
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
        "/ocr_url":   "Send the URL of the image you want to extract text from",
        "/stop": "",
        "/schedule": ""

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
        "/ocr_url": ocr_url,
        "/schedule": schedule,
        "/stop": stop
    }
    return command_service.get(command)



