class BlueskyEndpoints():

    def __init__(self, BSKY_SERVER):
        self.BSKY_SERVER = BSKY_SERVER
        if not self.BSKY_SERVER:
            self.BSKY_SERVER = "https://bsky.social"

    def get_url(self, path):
        return self.BSKY_SERVER + path
    
    #region com.atproto.admin
    def disableInviteCodes(self):
        return self.get_url("/xrpc/com.atproto.admin.disableInviteCodes")
        
    def getInviteCodes(self):
        return self.get_url("/xrpc/com.atproto.admin.getInviteCodes")

    def getModerationAction(self):
        return self.get_url("/xrpc/com.atproto.admin.getModerationAction")
    
    def getModerationActions(self):
        return self.get_url("/xrpc/com.atproto.admin.getModerationActions")
        
    def getModerationReport(self):
        return self.get_url("/xrpc/com.atproto.admin.getModerationReport")

    def getModerationReports(self):
        return self.get_url("/xrpc/com.atproto.admin.getModerationReports")
        
    def getAdminRecord(self):
        return self.get_url("/xrpc/com.atproto.admin.getRecord")
        
    def getRepo(self):
        return self.get_url("/xrpc/com.atproto.admin.getRepo")

    def resolveModerationReports(self):
        return self.get_url("/xrpc/com.atproto.admin.resolveModerationReports")
        
    def reverseModerationAction(self):
        return self.get_url("/xrpc/com.atproto.admin.reverseModerationAction")
        
    def searchRepos(self):
        return self.get_url("/xrpc/com.atproto.admin.searchRepos")
        
    def takeModerationAction(self):
        return self.get_url("/xrpc/com.atproto.admin.takeModerationAction")
        
    def updateAccountEmail(self):
        return self.get_url("/xrpc/com.atproto.admin.updateAccountEmail")

    def updateAccountHandle(self):
        return self.get_url("/xrpc/com.atproto.admin.updateAccountHandle")

    #endregion

    #region com.atproto.identity
    def resolveHandle(self):
        return self.get_url("/xrpc/com.atproto.identity.resolveHandle")

    def updateHandle(self):
        return self.get_url("/xrpc/com.atproto.identity.updateHandle")

    #endregion

    #region com.atproto.label
    def queryLabels(self):
        return self.get_url("/com.atproto.label.queryLabels")
    
    def subscribeLabels(self):
        return self.get_url("/com.atproto.label.subscribeLabels")
    #endregion

    #region com.atproto.repo
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

    #endregion

    #region com.atproto.server
    def createAccount(self):
        return self.get_url("/xrpc/com.atproto.server.createAccount")

    def createAppPassword(self):
        return self.get_url("/xrpc/com.atproto.server.createAppPassword")

    def createInviteCode(self):
        return self.get_url("/xrpc/com.atproto.server.createInviteCode")

    def createInviteCodes(self):
        return self.get_url("/xrpc/com.atproto.server.createInviteCodes")

    def createSession(self):
        return self.get_url("/xrpc/com.atproto.server.createSession")

    def deleteAccount(self):
        return self.get_url("/xrpc/com.atproto.server.deleteAccount")

    def deleteSession(self):
        return self.get_url("/xrpc/com.atproto.server.deleteSession")

    def describeServer(self):
        return self.get_url("/xrpc/com.atproto.server.describeServer")

    def getAccountInviteCodes(self):
        return self.get_url("/xrpc/com.atproto.server.getAccountInviteCodes")

    def getSession(self):
        return self.get_url("/xrpc/com.atproto.server.getSession")

    def listAppPasswords(self):
        return self.get_url("/xrpc/com.atproto.server.listAppPasswords")

    def resetPassword(self):
        return self.get_url("/xrpc/com.atproto.server.resetPassword")

    def refreshSession(self):
        return self.get_url("/xrpc/com.atproto.server.refreshSession")

    def requestAccountDelete(self):
        return self.get_url("/xrpc/com.atproto.server.requestAccountDelete")

    def requestPasswordReset(self):
        return self.get_url("/xrpc/com.atproto.server.requestPasswordReset")

    def revokeAppPassword(self):
        return self.get_url("/xrpc/com.atproto.server.revokeAppPassword")

    #endregion

    #region com.atproto.sync
    def getBlob(self):
        return self.get_url("/xrpc/com.atproto.sync.getBlob")
    
    def getBlocks(self):
        return self.get_url("/xrpc/com.atproto.sync.getBlocks")
    
    def getCheckout(self):
        return self.get_url("/xrpc/com.atproto.sync.getCheckout")
    
    def getCommitPath(self):
        return self.get_url("/xrpc/com.atproto.sync.getCommitPath")
    
    def getHead(self):
        return self.get_url("/xrpc/com.atproto.sync.getHead")
    
    def getSyncRecord(self):
        return self.get_url("/xrpc/com.atproto.sync.getRecord")
    
    def getRepo(self):
        return self.get_url("/xrpc/com.atproto.sync.getRepo")
    
    def listBlobs(self):
        return self.get_url("/xrpc/com.atproto.sync.listBlobs")
    
    def notifyOfUpdate(self):
        return self.get_url("/xrpc/com.atproto.sync.notifyOfUpdate")
    
    def requestCrawl(self):
        return self.get_url("/xrpc/com.atproto.sync.requestCrawl")
    
    def subscribeRepos(self):
        return self.get_url("/xrpc/com.atproto.sync.subscribeRepos")

    #endregion

    #region app.bsky.actor
    def getProfile(self):
        return self.get_url("/xrpc/app.bsky.actor.getProfile")

    def getProfiles(self):
        return self.get_url("/xrpc/app.bsky.actor.getProfiles")
    
    def getSuggestions(self):
        return self.get_url("/xrpc/app.bsky.actor.getSuggestions")
    
    def searchActors(self):
        return self.get_url("/xrpc/app.bsky.actor.searchActors")
    
    def searchActorsTypeahead(self):
        return self.get_url("/xrpc/app.bsky.actor.searchActorsTypeahead")
    #endregion

    #region app.bsky.feed
    def getAuthorFeed(self):
        return self.get_url("/xrpc/app.bsky.feed.getAuthorFeed")
    
    def getLikes(self):
        return self.get_url("/xrpc/app.bsky.feed.getLikes")

    def getPostThread(self):
        return self.get_url("/xrpc/app.bsky.feed.getPostThread")

    def getRepostedBy(self):
        return self.get_url("/xrpc/app.bsky.feed.getRepostedBy")

    def getTimeline(self):
        return self.get_url("/xrpc/app.bsky.feed.getTimeline")

    def like(self):
        return self.get_url("/xrpc/app.bsky.feed.like")
    
    def post(self):
        return self.get_url("/xrpc/app.bsky.feed.post")
    
    def repost(self):
        return self.get_url("/xrpc/app.bsky.feed.repost")
    #endregion

    #region app.bsky.graph
    def follow(self):
        return self.get_url("/xrpc/app.bsky.graph.follow")

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

    #endregion

    #region app.bsky.notification
    def getUnreadCount(self):
        return self.get_url("/xrpc/app.bsky.notification.getUnreadCount")

    def listNotifications(self):
        return self.get_url("/xrpc/app.bsky.notification.listNotifications")

    def updateSeen(self):
        return self.get_url("/xrpc/app.bsky.notification.updateSeen")

    #endregion

    #region app.bsky.richtext
    def facet(self):
        return self.get_url("/xrpc/app.bsky.richtext.facet")
    #endregion

    #region app.bsky.unspecced
    def getPopular(self):
        return self.get_url("/xrpc/app.bsky.unspecced.getPopular")

    #endregion

    #region health
    def health(self):
        return self.get_url("/xrpc/health")

    #endregion

