import confidential
from bot.TwitchBot import TwitchBotFactory, TwitchBot


class SpamTwitchBot(TwitchBot):
    pass


if __name__ == "__main__":
    factory = TwitchBotFactory(SpamTwitchBot, '#sjow', 'Esroh8', confidential.twitch_oauth)
