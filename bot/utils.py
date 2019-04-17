"""
    Helper functions to be used inside the project
"""
from .commands import start_command, help_command, weather, translate, calculate, tweet, ocr_url


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
