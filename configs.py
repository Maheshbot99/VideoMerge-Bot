# (c) @AbirHasan2005

import os


class Config(object):
    API_ID = os.environ.get("API_ID" 22525529)
    API_HASH = os.environ.get("API_HASH" 840111f82bbd1d2d3de5055afccf6a92)
    BOT_TOKEN = os.environ.get("BOT_TOKEN" 5946994770:AAGjUZjTbzUXfI1ArMGc-0gtdpnCdjSqnG8)
    SESSION_NAME = os.environ.get("SESSION_NAME", "BotTest_MsBot")
    UPDATES_CHANNEL = os.environ.get("UPDATES_CHANNEL" -1001790068959)
    LOG_CHANNEL = os.environ.get("LOG_CHANNEL" -1001790068959)
    DOWN_PATH = os.environ.get("DOWN_PATH", "./downloads")
    TIME_GAP = int(os.environ.get("TIME_GAP", 5))
    MAX_VIDEOS = int(os.environ.get("MAX_VIDEOS", 5))
    STREAMTAPE_API_USERNAME = os.environ.get("STREAMTAPE_API_USERNAME")
    STREAMTAPE_API_PASS = os.environ.get("STREAMTAPE_API_PASS")
    MONGODB_URI = os.environ.get("MONGODB_URI" mongodb+srv://Bot:Bot@cluster0.s0ppb5z.mongodb.net/?retryWrites=true&w=majority)
    BROADCAST_AS_COPY = bool(os.environ.get("BROADCAST_AS_COPY", False))
    BOT_OWNER = int(os.environ.get("BOT_OWNER", 5450011131))

    START_TEXT = """
Hi Unkil, I am Video Merge Bot!
I can Merge Multiple Videos in One Video. Video Formats should be same.

Made by @AbirHasan2005
"""
    CAPTION = "Video Merged by @{}\n\nMade by @AbirHasan2005"
    PROGRESS = """
Percentage : {0}%
Done: {1}
Total: {2}
Speed: {3}/s
ETA: {4}
"""
