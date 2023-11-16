"""Object validator for validate entering rows"""
import re
from datetime import datetime

import email_validator
from email_validator import validate_email


class Validator:
    """Object validator"""

    def __init__(self, value: str):
        self.value = value

    async def _email(self) -> bool:
        """Email validate"""
        v = self.value
        try:
            validate_email(v)
        except (
                email_validator.EmailSyntaxError,
                email_validator.EmailNotValidError,
                email_validator.EmailUndeliverableError
        ):
            return False
        return True

    async def _phone(self) -> bool:
        """Number of telephone validate"""
        rule = r"^\+7\s\d{3}\s\d{3}\s\d{2}\s\d{2}$"
        v = self.value
        if re.match(pattern=rule, string=v):
            return True
        return False

    async def _date(self) -> bool:
        """Datetime validate"""
        rules = [r"^\d{4}\:\d{2}\:\d{2}$", r"^\d{2}\:\d{2}\:\d{4}$"]
        v = self.value
        date1 = re.match(pattern=rules[0], string=v)
        date2 = re.match(pattern=rules[1], string=v)
        if date1:
            try:
                datetime.strptime(v, "%Y:%m:%d")
                return True
            except ValueError:
                return False
        elif date2:
            try:
                datetime.strptime(v, "%d:%m:%Y")
                return True
            except ValueError:
                return False
        return False

    @staticmethod
    async def parce(data: str) -> dict:
        """Parce query from URL"""
        new_data = data.replace("%20", " ")
        obj = new_data.split("&")
        res = {}
        for item in obj:
            row = item.split("=")
            res[row[0]] = row[1]
        return res

    async def validate(self) -> str:
        """Head coroutine for typing"""
        if await self._email():
            return "email"
        if await self._phone():
            return "phone"
        if await self._date():
            return "date"
        return "text"
