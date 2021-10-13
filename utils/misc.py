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
    ("dark.min.css", "Dark"),
    ("dracula.min.css", "Dracula"),
    ("tomorrow.min.css", "Tomorrow"),
    ("night-owl.min.css", "Night Owl"),
    ("codepen-embed.min.css", "Codepen"),
    ("github-gist.min.css", "Github Gist"),
    ("atom-one-dark.min.css", "Atom Dark"),
    ("solarized-dark.min.css", "Solarized Dark"),
    ("atelier-cave-dark.min.css", "Atelier Cave"),
    ("tomorrow-night-blue.css", "Tomorrow Night Blue",),
    ("atom-one-dark-reasonable.min.css", "Atom Dark Reasonable"),
)

page_theme_choices = (
    ("event-light-theme", "Light Theme"),
    ("event-dark-theme", "Dark Theme"),
    ("event-ares-theme", "Ares Theme"),
    ("event-nemesis-theme", "Nemesis Theme"),
    ("event-grass-hopper-theme", "Grasshopper Theme"),
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
