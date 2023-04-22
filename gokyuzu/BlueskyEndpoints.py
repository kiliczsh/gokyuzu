class BlueskyEndpoints():
    def __init__(self, BSKY_SERVER):
        self.BSKY_SERVER = BSKY_SERVER
        if not self.BSKY_SERVER:
            self.BSKY_SERVER = "https://bsky.social"

    def get_url(self, path):
        return self.BSKY_SERVER + path
    
    def createSession(self):
        return self.get_url("/xrpc/com.atproto.server.createSession")
    
    def resolveHandle(self):
        return self.get_url("/xrpc/com.atproto.identity.resolveHandle")
    
    def getProfile(self):
        return self.get_url("/xrpc/app.bsky.actor.getProfile")
    
    def createRecord(self):
        return self.get_url("/xrpc/com.atproto.repo.createRecord")
    
    def deleteRecord(self):
        return self.get_url("/xrpc/com.atproto.repo.deleteRecord")
    
    def getAccountInviteCodes(self):
        return self.get_url("/xrpc/com.atproto.server.getAccountInviteCodes")
    
    def getFollowers(self):
        return self.get_url("/xrpc/app.bsky.graph.getFollowers")
    
    def getFollows(self):
        return self.get_url("/xrpc/app.bsky.graph.getFollows")
    
    def listNotifications(self):
        return self.get_url("/xrpc/app.bsky.notification.listNotifications")
    
    def updateSeen(self):
        return self.get_url("/xrpc/app.bsky.notification.updateSeen")
