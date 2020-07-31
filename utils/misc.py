event_status = [
    ("Live", "Live"),
    ("Ended", "Ended"),
    ("Upcoming", "Upcoming"),
]

news_update_types = (
    ("News", "News"),
    ("Live", "Live"),
    ("Announcements", "Announcements")
)

event_types = (
    ("Other Event", "Other"),
    ("CTF Event", "CTF-Event"),
    ("Team Challenge", "Team-Challenge"),
    ("Coding Challenge", "Coding-Challenge")
)

status_css_class = [
    ('cata red', 'Started'),
    ('cata green', 'Upcoming'),
    ("cata yellow", "Completed"),
    ("cata purple", "Refactoring"),
]

code_hljs_styles = (
    ("Dark", "dark.min.css"),
    ("Dracula", "dracula.min.css"),
    ("Tomorrow", "tomorrow.min.css"),
    ("Night Owl", "night-owl.min.css"),
    ("Codepen", "codepen-embed.min.css"),
    ("Github Gist", "github-gist.min.css"),
    ("Atom Dark", "atom-one-dark.min.css"),
    ("Solarized Dark", "solarized-dark.min.css"),
    ("Atelier Cave", "atelier-cave-dark.min.css"),
    ("Tomorrow Night Blue", "tomorrow-night-blue.css"),
    ("Atom Dark Reasonable", "atom-one-dark-reasonable.min.css"),
)


def empty_array():
    return []


def empty_dict():
    return {}


def default_strikes():
    return {"AD": 0,
            "Racial": 0,
            "Homo": 0,
            "Common": 0
            }


def default_service_status():
    return {"status": "Offline",
            "last_down_time": "",
            "time_went_down": "",
            "time_back_online": ""
            }
