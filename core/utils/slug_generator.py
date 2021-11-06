import uuid
import random


class SlugGenerator:
    first_words = [
        "curious", "magical", "soft", "random", "bland",
        "bioluminescent", "serverless", "wholesome", "idle",
        "local", "detective", "faithless", "adamant", "anonymous"
        "bannable", "energetic", "punchable", "superstitious"

    ]

    last_words = [
        "cucumber", "butterfly", "poetry", "cactus", "abacus",
        "cuttlefish", "bay", "algae", "mushroom", "fish", "monkey",
        "turtle", "carrot", "squidward", "squid", "bob", "patrick",
        "mosquito", "duck", "ninja"
    ]

    @staticmethod
    def generate():
        return random.choice(SlugGenerator.first_words)\
               + random.choice(SlugGenerator.last_words) \
               + "-" + str(uuid.uuid4())[:5]
