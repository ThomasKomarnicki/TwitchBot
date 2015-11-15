import confidential
from bot.TwitchBot import TwitchBot
from bot.factory import TwitchBotFactory


class SpamTwitchBot(TwitchBot):
    pass


if __name__ == "__main__":
    factory = TwitchBotFactory(SpamTwitchBot, '#polt', 'Esroh8', confidential.twitch_oauth)
