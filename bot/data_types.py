"""
    Types stored in DB.
    Will be used to create instances of Users, Messages when retrieved from DB.
"""


class User:
    """User type"""
    def __init__(
            self,
            id: int,
            is_bot: bool,
            is_admin: bool,
            first_name: str,
            last_name: str,
            username: str,
            language_code: str,
            active: bool,
            created: int,
            updated: int,
            last_command: str):
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


class Message:
    """Message type"""
    def __init__(self, id: int, update_id: int, user_id: int, chat_id: int, date: int, text: str):
        self.id = id
        self.update_id = update_id
        self.user_id = user_id
        self.chat_id = chat_id
        self.date = date
        self.text = text


class Event:
    """Event type"""
    def __init__(self, id: int, time: int, description: str, cancelled: bool):
        self.id = id
        self.time = time
        self.description = description
        self.cancelled = bool(cancelled)


class ScheduleEntry:
    """Schedule Entry type"""
    def __init__(
            self,
            id: int,
            time: int,
            saturday: str, sunday: str, monday: str, tuesday: str, wednesday: str, thursday: str):
        self.id = id
        self.time = time
        self.saturday = saturday
        self.sunday = sunday
        self.monday = monday
        self.tuesday = tuesday
        self.wednesday = wednesday
        self.thursday = thursday
