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
    
    def getAccountInviteCodes(self):
        return self.get_url("/xrpc/com.atproto.server.getAccountInviteCodes")
    
    def createInviteCode(self):
        return self.get_url("/xrpc/com.atproto.server.createInviteCode")
    
    def createInviteCodes(self):
        return self.get_url("/xrpc/com.atproto.server.createInviteCodes")
    
    def describeServer(self):
        return self.get_url("/xrpc/com.atproto.server.describeServer")
    
    def deleteAccount(self):
        return self.get_url("/xrpc/com.atproto.server.deleteAccount")
    
    def resetPassword(self):
        return self.get_url("/xrpc/com.atproto.server.resetPassword")
    
    def requestPasswordReset(self):
        return self.get_url("/xrpc/com.atproto.server.requestPasswordReset")
    
    def createSession(self):
        return self.get_url("/xrpc/com.atproto.server.createSession")
    
    def deleteSession(self):
        return self.get_url("/xrpc/com.atproto.server.deleteSession")
    
    def getSession(self):
        return self.get_url("/xrpc/com.atproto.server.getSession")
    
    def refreshSession(self):
        return self.get_url("/xrpc/com.atproto.server.refreshSession")
    
    def createAppPassword(self):
        return self.get_url("/xrpc/com.atproto.server.createAppPassword")
    
    def listAppPassword(self):
        return self.get_url("/xrpc/com.atproto.server.listAppPassword")
    
    def revokeAppPassword(self):
        return self.get_url("/xrpc/com.atproto.server.revokeAppPassword")

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
    
    def getLikes(self):
        return self.get_url("/xrpc/app.bsky.feed.getLikes")
    
    def getRepostedBy(self):
        return self.get_url("/xrpc/app.bsky.feed.getRepostedBy")

    # app.bsky.graph    
    def getFollowers(self):
        return self.get_url("/xrpc/app.bsky.graph.getFollowers")
    
    def getFollows(self):
        return self.get_url("/xrpc/app.bsky.graph.getFollows")
    
    def getMutes(self):
        return self.get_url("/xrpc/app.bsky.graph.getMutes")
    
    def muteActor(self):
        return self.get_url("/xrpc/app.bsky.graph.muteActor")
    
    def unmuteActor(self):
        return self.get_url("/xrpc/app.bsky.graph.unmuteActor")
    
    # app.bsky.notification
    def listNotifications(self):
        return self.get_url("/xrpc/app.bsky.notification.listNotifications")
    
    def updateSeen(self):
        return self.get_url("/xrpc/app.bsky.notification.updateSeen")
    
    def getUnreadCount(self):
        return self.get_url("/xrpc/app.bsky.notification.getUnreadCount")
    
    # com.atproto.repo
    def applyWrites(self):
        return self.get_url("/xrpc/com.atproto.repo.applyWrites")

    def createRecord(self):
        return self.get_url("/xrpc/com.atproto.repo.createRecord")
    
    def deleteRecord(self):
        return self.get_url("/xrpc/com.atproto.repo.deleteRecord")
    
    def describeRepo(self):
        return self.get_url("/xrpc/com.atproto.repo.describeRepo")
    
    def getRecord(self):
        return self.get_url("/xrpc/com.atproto.repo.getRecord")
    
    def listRecords(self):
        return self.get_url("/xrpc/com.atproto.repo.listRecords")
    
    def putRecord(self):
        return self.get_url("/xrpc/com.atproto.repo.putRecord")
    
    def uploadBlob(self):
        return self.get_url("/xrpc/com.atproto.repo.uploadBlob")
    
    # com.atproto.identity
    def resolveHandle(self):
        return self.get_url("/xrpc/com.atproto.identity.resolveHandle")
    
    def updateHandle(self):
        return self.get_url("/xrpc/com.atproto.identity.updateHandle")
    
    # health
    def health(self):
        return self.get_url("/xrpc/health")

    # options
    def getAllEndpoints(self):
        all = []

        all.append(self.createAccount())
        all.append(self.createSession())
        all.append(self.getSession())
        all.append(self.getAccountInviteCodes())
        all.append(self.getProfile())
        all.append(self.getProfiles())
        all.append(self.getPopular())
        all.append(self.getTimeline())
        all.append(self.getAuthorFeed())
        all.append(self.getPostThread())
        all.append(self.getFollowers())
        all.append(self.getFollows())
        all.append(self.listNotifications())
        all.append(self.updateSeen())
        all.append(self.createRecord())
        all.append(self.deleteRecord())
        all.append(self.resolveHandle())
        all.append(self.updateHandle())
        all.append(self.getRecord())
        all.append(self.listRecords())
        all.append(self.putRecord())
        all.append(self.uploadBlob())
        all.append(self.applyWrites())
        all.append(self.describeRepo())
        all.append(self.getUnreadCount())
        all.append(self.getFollowers())
        all.append(self.getFollows())
        all.append(self.getMutes())
        all.append(self.muteActor())
        all.append(self.unmuteActor())
        all.append(self.describeServer())
        all.append(self.deleteAccount())
        all.append(self.resetPassword())
        all.append(self.requestPasswordReset())
        all.append(self.deleteSession())
        all.append(self.refreshSession())
        all.append(self.createAppPassword())
        all.append(self.listAppPassword())
        all.append(self.revokeAppPassword())
        all.append(self.health())

        return all

    


