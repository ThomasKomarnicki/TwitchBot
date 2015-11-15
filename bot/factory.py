from twisted.internet import protocol, reactor, defer


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

    @type channel: C{str}
    @param channel: the channel name prepended with a '#' i.e. '#forsenlol'

    @type bot_class: C{str}
    @param bot_class: your twitch username

    @type bot_class: C{str}
    @param bot_class: your twitch oauth string which can be generated here: http://www.twitchapps.com/tmi
    """
    def __init__(self, bot_class, channel, twitch_username, twitch_oauth):
        factory = _BotFactory(bot_class, channel, twitch_username, twitch_oauth)
        reactor.connectTCP('irc.twitch.tv', 6667, factory)
        reactor.run()

