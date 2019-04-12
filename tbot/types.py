"""
    Types stored in DB.
    Will be used to create instances of Users, Messages when retrieved from DB.
"""


class User:
    """User type"""
    def __init__(
            self,
            id,
            is_bot,
            is_admin,
            first_name,
            last_name,
            username,
            language_code,
            active,
            created,
            updated,
            last_command):
        self.id = id
        self.is_bot = is_bot
        self.is_admin = is_admin
        self.first_name = first_name
        self.last_name = last_name
        self.username = username
        self.language_code = language_code
        self.active = active
        self.created = created
        self.updated = updated
        self.last_command = last_command


class Message:
    """Message type"""
    def __init__(self, id, update_id, user_id, chat_id, date, text):
        self.id = id
        self.update_id = update_id
        self.user_id = user_id
        self.chat_id = chat_id
        self.date = date
        self.text = text
