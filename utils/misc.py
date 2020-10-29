from django.db import models


class DiscordIDField(models.BigIntegerField):
    MIN_ID = 100000000000000000
    MAX_ID = 999999999999999999

    def __init__(self, **kwargs):
        if kwargs.get("primary_key") is not None:
            super().__init__(**kwargs)
        else:
            super().__init__(null=True, blank=True, **kwargs)

    def formfield(self, **kwargs):
        return super().formfield(**{
            "min_value": DiscordIDField.MIN_ID,
            "max_value": DiscordIDField.MAX_ID,
            **kwargs,
        })


def empty_array():
    return []


def empty_dict():
    return {}


def default_strikes():
    return {
        "AD": 0,
        "Racial": 0,
        "Homo": 0,
        "Common": 0
    }


def default_service_status():
    return {
        "status": "Offline",
        "last_down_time": "",
        "time_went_down": "",
        "time_back_online": ""
    }
