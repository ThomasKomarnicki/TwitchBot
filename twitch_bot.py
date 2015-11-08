from twisted.words.protocols import irc
from twisted.internet import protocol, reactor
import confidential


class TwitchBot(irc.IRCClient):

    password = confidential.twitch_oauth # for twitch

    def _get_nickname(self):
        return self.factory.nickname
    nickname = property(_get_nickname)

    def signedOn(self):
        self.join(self.factory.channel)
        print "Signed on as %s." % (self.nickname,)

    def joined(self, channel):
        print "Joined %s." % (channel,)

    def privmsg(self, user, channel, msg):
        print msg


class TwitchBotFactory(protocol.ClientFactory):
    protocol = TwitchBot

    def __init__(self, channel, nickname='Esroh8'):
        self.channel = channel
        self.nickname = nickname

    def clientConnectionLost(self, connector, reason):
        print "Lost connection (%s), reconnecting." % (reason,)
        connector.connect()

    def clientConnectionFailed(self, connector, reason):
        print "Could not connect: %s" % (reason,)

if __name__ == "__main__":
    reactor.connectTCP('irc.twitch.tv', 6667, TwitchBotFactory('#sjow'))
    reactor.run()