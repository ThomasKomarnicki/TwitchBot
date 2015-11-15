import requests
from threading import Thread


class WatchersTask(Thread):
    '''
    @type bot: C{TwitchBot}
    @param bot: the twitch bot to call on once the task is complete
    '''
    def __init__(self, bot):
        ''' Constructor. '''
        Thread.__init__(self)
        self.bot = bot

    def run(self):
        print "starting watchers thread"
        self.fetch_watchers()

    def fetch_watchers(self):
        request = requests.get('http://tmi.twitch.tv/group/user/' + self.bot.get_clean_channel_name() + '/chatters')
        print request
        chatters_response = request.json()
        mods_array = chatters_response['chatters']['moderators']
        mods_array += chatters_response['chatters']['staff']
        mods_array += chatters_response['chatters']['admins']
        mods_array += chatters_response['chatters']['global_mods']
        self.bot.watchers_received(mods_array,chatters_response['chatters']['viewers'])