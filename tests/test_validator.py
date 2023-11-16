from src.database.validator import Validator


class TestValidator:
    async def test_email_validator(self):
        assert await Validator("example@gmail.com")._email() is True
        assert await Validator("example@example.example")._email() is False

    async def test_phone_validator(self):
        assert await Validator("+7 123 456 78 90")._phone() is True
        assert await Validator("+7 123 456 78 90 1")._phone() is False

    async def test_date_validator(self):
        assert await Validator("01:01:1990")._date() is True
        assert await Validator("1990:01:01")._date() is True
        assert await Validator("01:13:1990")._date() is False
        assert await Validator("1990:13:01")._date() is False

    async def test_main_validator(self):
        assert await Validator("01:01:1990").validate() == "date"
        assert await Validator("+7 123 456 78 90").validate() == "phone"
        assert await Validator("example@gmail.com").validate() == "email"
        assert await Validator("1990:13:01").validate() == "text"
        assert await Validator("+7 123 456 78 90 1").validate() == "text"
        assert await Validator("example@example.example").validate() == "text"

    async def test_parce_validator(self):
        example = "f_name1=value1&f_name2=value2&phone=+7%20123%20456%2078%2090"
        assert await Validator.parce(example) == {
            "f_name1": "value1",
            "f_name2": "value2",
            "phone": "+7 123 456 78 90"
        }
