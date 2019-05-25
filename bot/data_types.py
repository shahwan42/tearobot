"""
    Types stored in DB.
    Will be used to create instances of Users, Messages when retrieved from DB.
"""


class User:
    """User type"""
    def __init__(self, id: int, is_bot: bool, is_admin: bool, first_name: str, last_name: str, username: str,
                 language_code: str, active: bool, created: int, updated: int, last_command: str, chat_id: int):
        self.id = id
        self.is_bot = bool(is_bot)
        self.is_admin = bool(is_admin)
        self.first_name = first_name
        self.last_name = last_name
        self.username = username
        self.language_code = language_code
        self.active = bool(active)
        self.created = created
        self.updated = updated
        self.last_command = last_command
        self.chat_id = chat_id

    def __str__(self):
        return f"[<User>: id: {self.id}, is_bot: {self.is_bot}, is_admin: {self.is_admin}, " \
               f"first_name: {self.first_name}, last_name: {self.last_name}, username: {self.username}, " \
               f"language_code: {self.language_code}, active: {self.active}, created: {self.created}, " \
               f"updated: {self.updated}, last_command: {self.last_command}, chat_id: {self.chat_id}]"


class Message:
    """Message type"""
    def __init__(self, id: int, update_id: int, user_id: int, chat_id: int, date: int, text: str):
        self.id = id
        self.update_id = update_id
        self.user_id = user_id
        self.chat_id = chat_id
        self.date = date
        self.text = text

    def __str__(self):
        return f"[<Message>: id: {self.id}, update_id: {self.update_id}, user_id: {self.user_id}, " \
               f"chat_id: {self.chat_id}, date: {self.date}, text: {self.text}]"


class Announcement:
    """Event type"""
    def __init__(self, time: str, description: str, done: str, id: int = None):
        self.time = time
        self.description = description
        self.done = done
        self.id = id

    def __str__(self):
        return f"[<Event>: id: {self.id}, time: {self.time}, description: {self.description}, " \
               f"cancelled: {self.done}]"


class ScheduleEntry:
    """Schedule Entry type"""
    def __init__(self, time: int, subject: str, day: str, id: int = None):
        self.id = id
        self.time = time
        self.subject = subject
        self.day = day

    def __str__(self):
        return f"[<ScheduleEntry>: id: {self.id}, time: {self.time}, subject: {self.subject}, " \
               f"day: {self.day}]"
