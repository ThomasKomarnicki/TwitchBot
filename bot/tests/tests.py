from test import test_support
from bot import TwitchBot
import unittest


class TestBot(TwitchBot):

    def chat_message(self, user, message):
        assert 'test' == user

    def bot_message(self, user, command, message):
        assert 'test' == user
        assert '!TwitchBot' == command

    def watchers_received(self, mods, watchers):
        pass



class TwitchBotTest(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_bot_commands(self):
        bot = TwitchBot()
        bot.privmsg('test!test@test.tmi.twitch.tv', '#test', 'message goes here')
        bot.privmsg('test!test@test.tmi.twitch.tv', '#test', '!TwitchBot please help')


if __name__ == '__main__':
    test_support.run_unittest(TwitchBotTest)