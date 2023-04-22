class BlueskyEndpoints():
    def __init__(self, BSKY_SERVER):
        self.BSKY_SERVER = BSKY_SERVER
        if not self.BSKY_SERVER:
            self.BSKY_SERVER = "https://bsky.social"

    def get_url(self, path):
        return self.BSKY_SERVER + path
    
    # com.atproto.server
    def createAccount(self):
        return self.get_url("/xrpc/com.atproto.server.createAccount")

    def createSession(self):
        return self.get_url("/xrpc/com.atproto.server.createSession")
    
    def getSession(self):
        return self.get_url("/xrpc/com.atproto.server.getSession")
    
    def getAccountInviteCodes(self):
        return self.get_url("/xrpc/com.atproto.server.getAccountInviteCodes")
    
    # app.bsky.actor
    def getProfile(self):
        return self.get_url("/xrpc/app.bsky.actor.getProfile")
    
    def getProfiles(self):
        return self.get_url("/xrpc/app.bsky.actor.getProfiles")
    
    # app.bsky.unspecced
    def getPopular(self):
        return self.get_url("/xrpc/app.bsky.unspecced.getPopular")
    
    # app.bsky.feed
    def getTimeline(self):
        return self.get_url("/xrpc/app.bsky.feed.getTimeline")
    
    def getAuthorFeed(self):
        return self.get_url("/xrpc/app.bsky.feed.getAuthorFeed")
    
    def getPostThread(self):
        return self.get_url("/xrpc/app.bsky.feed.getPostThread")
    
    # app.bsky.graph    
    def getFollowers(self):
        return self.get_url("/xrpc/app.bsky.graph.getFollowers")
    
    def getFollows(self):
        return self.get_url("/xrpc/app.bsky.graph.getFollows")
    
    # app.bsky.notification
    def listNotifications(self):
        return self.get_url("/xrpc/app.bsky.notification.listNotifications")
    
    def updateSeen(self):
        return self.get_url("/xrpc/app.bsky.notification.updateSeen")
    
    # com.atproto.repo
    def createRecord(self):
        return self.get_url("/xrpc/com.atproto.repo.createRecord")
    
    def deleteRecord(self):
        return self.get_url("/xrpc/com.atproto.repo.deleteRecord")
    
    # com.atproto.identity
    def resolveHandle(self):
        return self.get_url("/xrpc/com.atproto.identity.resolveHandle")
    
    def updateHandle(self):
        return self.get_url("/xrpc/com.atproto.identity.updateHandle")


