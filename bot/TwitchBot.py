from twisted.words.protocols import irc
from tasks import WatchersTask
import re


class TwitchBot(irc.IRCClient):
    #
    bot_commands = re.compile('(\!TwitchBot)|(\!BotTwitch)')

    def _get_nickname(self):
        return self.factory.nickname
    nickname = property(_get_nickname)

    def get_clean_channel_name(self):
        return self.factory.channel[1:]

    def signedOn(self):
        self.join(self.factory.channel)
        print "Signed on as %s." % (self.nickname,)

    def get_watchers(self):
        watchers_thread = WatchersTask(self)
        watchers_thread.start()

    def joined(self, channel):
        print "Joined %s." % (channel,)

    def privmsg(self, user, channel, msg):
        # print str(user) + ':::: ' + str(msg) + '\n'
        user = self.create_twitch_name(user)
        if self.bot_commands and self.bot_commands.match(msg):
            m = self.bot_commands.search(msg)
            command = m.group(0)
            self.bot_message(user, command, msg[len(command):])
        else:
            self.chat_message(user, msg)

    def create_twitch_name(self, user):
        return re.compile('\!').split(user)[0]




    # bot methods intened to be overridden

    def chat_message(self, user, message):
        pass

    def bot_message(self, user, command, message):
        '''
        called when a bot specific message has been triggered
        for the message "!TwitchBot hello", @param command: would be "!TwitchBot" and @param message: would be "hello"
        :param user: the user that sent the message
        :param command: the command associated with the message
        :param message: the remaind of the message
        :return:
        '''
        pass

    def watchers_received(self, mods, watchers):
        pass
        # print "mods"
        # print mods
        # print "watchers"
        # print watchers






