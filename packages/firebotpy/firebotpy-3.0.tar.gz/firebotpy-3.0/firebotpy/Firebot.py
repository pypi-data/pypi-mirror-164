import requests
import json

#This is the number of attemps that will be attempted before the request fails
totalAttempts = 3

#Not much error handling in this so always use proper capitalization when using any method


class Firebot:


    def __init__(self, url='http://localhost:7472/api/v1'): #If the bot is being ran on another computer make sure you change this
        self.url = url


    def get_status(self):
        """
        Returns a True of False based on the connection status of firebot 
        """
        r = requests.get(self.url+"/status")
        return bool(r.json()['connections']['chat'])
    

    def get_effects(self):
        """
        Returns a list with all the effects within firebot
        """
        r = requests.get(self.url+"/effects")
        print(r.json())


    def post(self, data):
        """
        Used to post the request to the bot. 
        """
        attempts = 0
        while attempts <= totalAttempts:
            try:
                r = requests.post(f"{self.url}/effects/",
                                         headers={"content-type": "application/json"}, data=json.dumps(data))
                return r.json()
            except:
                attempts += 1


    def get_presetEffectID(self, name):
        """
        Returns the ID of a preset effect list.
        """
        r = requests.get(self.url+"/effects/preset")
        data = r.json()
        for effect in data:
            effectName = effect['name']
            if effectName == name:
                return effect['id']


    def get_allPresetEffects(self):
        """
        Returns all the preset effects currently in firebot
        """
        attempts = 0
        while attempts <= totalAttempts:
            try:
                r = requests.get(self.url+"/effects/preset")
                return r.json()
            except:
                attempts += 1
                

    def get_allViewers(self):
        """
        Returns a list of all the users stored in firebots database
        """
        attempts = 0
        while attempts <= totalAttempts:
            try:
                r = requests.get(self.url+"/viewers")
                return r.json()
            except:
                attempts += 1


    def get_viewerID(self, user):
        """
        Returns a the id associated with a user in firebots database
        """
        data = self.get_allViewers()
        for x in data:
            username = x['username'].lower()
            if username == user.lower():
                return x['id']


    def get_allUserMetadata(self, user):
        """
        Returns all the metadata from firebots database
        """
        id = self.get_viewerID(user)
        if id != None:
            attempts = 0
            while attempts <= totalAttempts:
                try:
                    r = requests.get(self.url+"/viewers/"+id)
                    return r.json()
                except:
                    attempts += 1
        else:
            return None


    def get_userMetadata(self, user, metadata):
        """
        Returns the value of metadata for a user. Metadata postional argument is case sensitive. 
        """
        id = self.get_viewerID(user)
        if id != None:
            attempts = 0
            while attempts <= totalAttempts:
                try:
                    data = self.get_allUserMetadata(user)
                    return data['metadata'][metadata]
                except:
                    attempts += 1
        else:
            return None


    def get_allCurrencyID(self):
        """
        Returns a list of all the currency ID's stored in firebots database
        """
        attempts = 0
        while attempts <= totalAttempts:
            try:
                r = requests.get(self.url+"/currency")
                return r.json()
            except:
                attempts += 1


    def get_currencyID(self, currency):
        """
        Returns the currency ID of the given currency
        """
        data = self.get_allCurrencyID()
        for x in data:
            if currency == data[x]['name']:
                return data[x]['id']


    def get_topCurrency(self, currency, count = 10):
        """
        Returns a list of the users with the top amount in a currency. Defaults to 10.
        """
        id = self.get_currencyID(currency)
        if id != None:
            attempts = 0
            while attempts <= totalAttempts:
                try:
                    r = requests.get(self.url+f"/currency/points/top?count={count}")
                    currency_list = []
                    for users in r.json():
                        userdict = {}
                        username = users['username']
                        amount = users['currency'][id]
                        userdict = {'username': username, 'amount': amount}
                        currency_list.append(userdict)
                    return currency_list
                except:
                    attempts += 1


    def get_userCurrency(self, user, currency):
        """
        Returns the amount a user has of the given currency
        """
        id = self.get_currencyID(currency)
        if id != None:
            attempts = 0
            while attempts <= totalAttempts:
                try:
                    r = requests.get(self.url+f"/viewers/{user}/currency/{id}?username=true")
                    return r.json()
                except:
                    attempts += 1


    def set_userCurrency(self, user, currency, amount):
        """
        Sets the currency amount for a user
        """
        id = self.get_currencyID(currency)
        data = {
            "effects": {
                "list": [
                    {
                        "type": "firebot:currency",
                        "action": "Set",
                        "currency": id,
                        "amount": amount,
                        "target": "individual",
                        "userTarget": user
                    }
                ]
            }
        }
        if id != None:
            return self.post(data)


    def get_allVariables(self):
        """
        Returns the value of all variables stored in firebots database. DO NOT RECOMMEND RUNNING THIS AS IT IS A LOT OF DATA
        """
        if id != None:
            attempts = 0
            while attempts <= totalAttempts:
                try:
                    r = requests.get(self.url+f"/custom-variables")
                    return r.json()
                except:
                    attempts += 1


    def get_variable(self, variable):
        """
        Returns the value of a variable stored in firebots database
        """
        if id != None:
            attempts = 0
            while attempts <= totalAttempts:
                try:
                    r = requests.get(self.url+f"/custom-variables/{variable}")
                    return r.json()
                except:
                    attempts += 1


    def get_userRoles(self, user):
        """
        Returns a list of roles the user is assigned to
        """
        role_list = []
        for role in self.get_allUserMetadata(user)['customRoles']:
            role_list.append(role['name'])
        return role_list


    def get_userProfilePic(self, user):
        """
        Returns the link to the users profile pic
        """
        return self.get_allUserMetadata(user)['profilePicUrl']


    def get_userModStatus(self, user):
        """
        Returns either a True or False if the user is assigned as a mod
        """
        if 'mod' in self.get_allUserMetadata(user)['twitchRoles']:
            return True
        else:
            return False


    def add_currency(self, currency, amount, username):
        """
        Add currency to a user.
        """
        currencyid = self.get_currencyID(currency)
        data = {
            "effects": {
                "list": [
                    {
                        "type": "firebot:currency",
                        "action": "Add",
                        "currency": currencyid,
                        "amount": amount,
                        "target": "individual",
                        "userTarget": username
                    }
                ]
            }
        }
        self.post(data)


    def subtractCurrency(self, currency, amount, username):
        """
        Subtracts currency from a user.
        """
        currencyid = self.get_currencyID(currency)
        data = {
            "effects": {
                "list": [
                    {
                        "type": "firebot:currency",
                        "action": "Remove",
                        "currency": currencyid,
                        "amount": amount,
                        "target": "individual",
                        "userTarget": username
                    }
                ]
            }
        }
        self.post(data)


    def chatFeedAlert(self, message):
        """
        Send a chat feed alert.
        """
        data = {
            "effects": {
                "list": [
                    {
                        "type": "firebot:chat-feed-alert",
                        "message": message,
                    }
                ]
            }
        }
        self.post(data)


    def addVip(self, username):
        """
        Add a user to VIP.
        """
        data = {
            "effects": {
                "list": [
                    {
                        "type": "firebot:update-vip-role",
                        "action": "Add VIP",
                        "username": username
                    }
                ]
            }
        }
        self.post(data)


    def removeVip(self, username):
        """
        Remove a user from VIP.
        """
        data = {
            "effects": {
                "list": [
                    {
                        "type": "firebot:update-vip-role",
                        "action": "Remove VIP",
                        "username": username
                    }
                ]
            }
        }
        self.post(data)


    def banUser(self, username):
        """
        Ban a user.
        """
        data = {
            "effects": {
                "list": [
                    {
                        "type": "firebot:modban",
                        "action": "Ban",
                        "username": username
                    }
                ]
            }
        }
        self.post(data)


    def unbanUser(self, username):
        """
        Unban a user.
        """
        data = {
            "effects": {
                "list": [
                    {
                        "type": "firebot:modban",
                        "action": "Unban",
                        "username": username
                    }
                ]
            }
        }
        self.post(data)


    def changeObsScene(self, scene):
        """
        Change scenes in OBS. Must have the custom script installed
        """
        data = {
            "effects": {
                "list": [
                    {
                        "type": "ebiggz:obs-change-scene",
                        "custom": True,
                        "sceneName": scene,
                    }
                ]
            }
        }
        self.post(data)


    def setMetadata(self, key, data, username):
        """
        Set the metadata for a user.
        """
        data = {
            "effects": {
                "list": [
                    {
                        "type": "firebot:set-user-metadata",
                        "username": username,
                        "key": key,
                        "data": data,
                    }
                ]
            }
        }
        self.post(data)


    def announcement(self, message, chatter = 'bot'):
        """
        Sends an announcement message. Can be sent from the streamer account or the bot account. 
        Default is bot. Change chatter to anything else for it to send from streamer account
        """
        if chatter == 'bot':
            data = {
                "effects": {
                    "list": [
                        {
                            "type": "firebot:announcement",
                            "active": 'true',
                            "chatter":'bot',
                            "message": message,
                        }
                    ]
                }
            }
        else:
            data = {
                "effects": {
                    "list": [
                        {
                            "type": "firebot:announcement",
                            "active": 'true',
                            "chatter":'streamer',
                            "message": message,
                        }
                    ]
                }
            }
        self.post(data)


    def removeMetaData(self, username, key):
        """
        Removes metadata from the from a user
        """
        data = {
            "effects": {
                "list": [
                    {
                        "type": "firebot:remove-user-metadata",
                        "active": 'true',
                        "username": username,
                        "key": key,
                    }
                ]
            }
        }
        self.post(data)


    def setStreamTitle(self, title):
        """
        Sets the stream title
        """
        data = {
            "effects": {
                "list": [
                    {
                        "type": "firebot:streamtitle",
                        "active": 'true',
                        "title": title,
                    }
                ]
            }
        }
        self.post(data)


    def timeoutUser(self, username, time):
        """
        Timeout a user
        """
        data = {
            "effects": {
                "list": [
                    {
                        "type": "firebot:modTimeout",
                        "active": 'true',
                        "username": username,
                        "time": time,
                    }
                ]
            }
        }
        self.post(data)


    def botChat(self, message):
        """
        Sends a chat message as the bot account
        """
        data = {
            "effects": {
                "list": [
                    {
                        "chatter": "bot",
                        "type": "firebot:chat",
                        "active": 'true',
                        "message": message,
                    }
                ]
            }
        }
        self.post(data)


    def streamerChat(self, message):
        """
        Sends a chat message as the streamer account
        """
        data = {
            "effects": {
                "list": [
                    {
                        "chatter": "streamer",
                        "type": "firebot:chat",
                        "active": 'true',
                        "message": message,
                    }
                ]
            }
        }
        self.post(data)


    def customVariable(self, varname, vardata, duration=0):
        """
        Sets the value of a custom variable.
        """
        data = {
            "effects": {
                "list": [
                    {
                        "type": "firebot:customvariable",
                        "ttl": duration,
                        "name": varname,
                        "variableData": vardata,
                    }
                ]
            }
        }
        self.post(data)


    def fireworks(self, duration=6):
        """
        Trigger the fireworks celebration. Default duration is 6 seconds. 
        """
        data = {
            "effects": {
                "list": [
                    {
                        "type": "firebot:celebration",
                        "celebration": "Fireworks",
                        "length": duration,
                    }
                ]
            }
        }
        self.post(data)


    def confetti(self, duration=6):
        """
        Trigger the confetti celebration. Default duration is 6 seconds. 
        """
        data = {
            "effects": {
                "list": [
                    {
                        "type": "firebot:celebration",
                        "celebration": "Confetti",
                        "length": duration,
                    }
                ]
            }
        }
        self.post(data)


    def presetEffectList(self, name, arg="null", argdata="null", arg2="null", arg2data="null", arg3="null", arg3data="null", arg4="null", arg4data="null", arg5="null", arg5data="null"):
        """
        Triggers a given preset effect list. Able to pass in preset args as well.
        """
        id = self.get_presetEffectID(name)
        if id != None:
            presetarg = {
                "args": {
                    arg: argdata,
                    arg2: arg2data,
                    arg3: arg3data,
                    arg4: arg4data,
                    arg5: arg5data}
            }
            attempts = 0
            while attempts <= 5:
                try:
                    r = requests.post(f"{self.url}/effects/preset/{str(id)}",
                                    headers={"content-type": "application/json"}, data=json.dumps(presetarg))
                    if r.json()['status'] == 'success':
                        return 'Success'
                except:
                    attempts += 1


    def awsPolly(self, message, voiceid, volume):
        """
        Sends a message to Amazon Polly. Must have Amazon Polly set up in firebot
        """
        data = {
            "effects": {
                "list": [
                    {
                        "type": "aws:polly",
                        "text": message,
                        "voiceId": voiceid,
                        "volume": volume,
                    }
                ]
            }
        }
        self.post(data)


    def disableAllConnections(self):
        """
        Disables all firebot connections
        """
        data = {
            "effects": {
                "list": [
                    {
                        "type": "firebot:toggleconnection",
                        "allAction": "false",
                        "services": [
                            {
                                "id": "chat",
                                "action": True
                            }
                        ],
                        "mode": "all",
                    }
                ]
            }
        }
        self.post(data)


    def enableTwitchConnection(self):
        """
        Turn on Twitch connection.
        """
        data = {
            "effects": {
                "list": [
                    {
                        "type": "firebot:toggleconnection",
                        "allAction": "toggle",
                        "services": [
                            {
                                "id": "chat",
                                "action": True
                            }
                        ],
                        "mode": "custom",
                    }
                ]
            }
        }
        self.post(data)


    def disableTwitchConnection(self):
        """
        Turn off Twitch connection.
        """
        data = {
            "effects": {
                "list": [
                    {
                        "type": "firebot:toggleconnection",
                        "allAction": "toggle",
                        "services": [
                            {
                                "id": "chat",
                                "action": False
                            }
                        ],
                        "mode": "custom",
                    }
                ]
            }
        }
        self.post(data)


    def whisperChatstreamer(self, username, chatmessage):
        """
        Send a whisper message as the streamer. Be very careful how you use this. Also per firebot and twitch API this does not work 100% of the time
        """
        data = {
            "effects": {
                "list": [
                    {
                        "type": "firebot:chat",
                        "chatter": "Streamer",
                        "whisper": username,
                        "message": chatmessage,
                    }
                ]
            }
        }
        self.post(data)


    def whisperChatbot(self, username, chatmessage):
        """
        Send a whisper message as the bot. Be very careful how you use this. Also per firebot and twitch API this does not work 100% of the time
        """
        data = {
            "effects": {
                "list": [
                    {
                        "type": "firebot:chat",
                        "chatter": "Bot",
                        "whisper": username,
                        "message": chatmessage,
                    }
                ]
            }
        }
        self.post(data)


    def addCurrencyOnline(self, currency, amount):
        """
        Adds currency to all online viewers
        """
        currencyid = self.get_currencyID(currency)
        data = {
            "effects": {
                "list": [
                    {
                        "type": "firebot:currency",
                        "action": "Add",
                        "currency": currencyid,
                        "amount": amount,
                        "target": "allOnline",
                    }
                ]
            }
        }
        self.post(data)


    def removeCurrencyOnline(self, currency, amount):
        """
        Removes currency from all online viewers
        """
        currencyid = self.get_currencyID(currency)
        data = {
            "effects": {
                "list": [
                    {
                        "type": "firebot:currency",
                        "action": "Remove",
                        "currency": currencyid,
                        "amount": amount,
                        "target": "allOnline",
                    }
                ]
            }
        }
        self.post(data)


    def get_quotes(self):
        """
        Returns a list of all the quotes stored in firebots database
        """
        attempts = 0
        while attempts <= totalAttempts:
            try:
                r = requests.get(self.url+f"/quotes")
                return r.json()
            except:
                attempts += 1


    def addQuote(self, quote, creator, originator):
        """
        Removes currency from all online viewers
        """
        data = {
            "effects": {
                "list": [
                    {
                        "id": "cdd20130-2510-11ed-94f1-53812e8ae25e",
                        "type": "firebot:add-quote",
                        "active": 'true',
                        "creator": creator,
                        "text": quote,
                        "originator": originator,
                    }
                ]
            }
        }
        self.post(data)

