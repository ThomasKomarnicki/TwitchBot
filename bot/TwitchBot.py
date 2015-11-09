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
        print str(user) + ':::: ' + str(msg) + '\n\n'




class _BotFactory(protocol.ClientFactory):

    def __init__(self, bot_class, channel, twitch_username, twitch_oauth):
        self.protocol = bot_class
        self.twitch_oauth = twitch_oauth
        self.channel = channel
        self.nickname = twitch_username

    def clientConnectionLost(self, connector, reason):
        print "Lost connection (%s), reconnecting." % (reason,)
        connector.connect()

    def clientConnectionFailed(self, connector, reason):
        print "Could not connect: %s" % (reason,)

    def buildProtocol(self, addr):
        p = self.protocol()
        p.factory = self
        p.password = self.twitch_oauth
        return p


class TwitchBotFactory:

    """
    Called with creation date information about the server, usually at logon.

    @type bot_class: C{TwitchBot}
    @param bot_class: A class that extends TwitchBot that defines
    """
    def __init__(self, bot_class, channel, twitch_username, twitch_oauth):
        factory = _BotFactory(bot_class, channel, twitch_username, twitch_oauth)
        reactor.connectTCP('irc.twitch.tv', 6667, factory)
        reactor.run()







