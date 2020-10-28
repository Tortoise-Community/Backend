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
