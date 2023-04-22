import json
from types import SimpleNamespace
from gokyuzu.BlueskyEndpoints import BlueskyEndpoints
from gokyuzu.BlueskyHelper import BlueskyHelper
from gokyuzu.BlueskySession import BlueskySession


class Bluesky():
    def __init__(self, handle, password):
        self.BSKY_SERVER = "https://bsky.social"
        self.ENDPOINTS = BlueskyEndpoints(self.BSKY_SERVER)
        self.SESSION = BlueskySession(handle=handle, password=password)

    def __str__(self):
        return f"Bluesky(server={self.BSKY_SERVER}, handle={self.SESSION.getHandle()}, email={self.SESSION.getEmail()}, did={self.SESSION.getDID()}, accessToken={self.SESSION.getAccessToken()}, refreshToken={self.SESSION.getRefreshToken()})"

    # com.atproto.server
    def createAccount(self, email, handle, password, inviteCode):
        request_data = {
            "email": email,
            "handle": handle,
            "password": password,
            "inviteCode": inviteCode
        }

        response = self.SESSION.postJson(self.ENDPOINTS.createAccount(), json=request_data)
        return response
    
    def getSession(self):
        request_url = self.ENDPOINTS.getSession()
        response = self.SESSION.get(request_url)
        return response
    
    def getAccountInviteCodes(self, limit=10):
        request_url = self.ENDPOINTS.getAccountInviteCodes() + "?limit={}".format(limit)
        response = self.SESSION.get(request_url)
        return response

    # app.bsky.actor
    def getProfile(self, user_did):
        request_url = self.ENDPOINTS.getProfile() + "?actor={}".format(user_did)
        response = self.SESSION.get(request_url)
        return response
    
    def getProfiles(self, user_dids):
        request_url = self.ENDPOINTS.getProfiles() + "?actors={}".format(user_dids)
        response = self.SESSION.get(request_url)
        return response
    
    # app.bsky.unspecced
    def getPopular(self, limit=10, cursor=""):
        request_url = self.ENDPOINTS.getPopular() + "?limit={}&cursor={}".format(limit, cursor)
        response = self.SESSION.get(request_url)
        return response
    
    # app.bsky.feed
    def getTimeline(self, limit=10, cursor="", algorithm="reverse-chronological"):
        request_url = self.ENDPOINTS.getTimeline() + "?algorithm={}&limit={}&cursor={}".format(algorithm, limit, cursor)
        response = self.SESSION.get(request_url)
        return response
    
    def getAuthorFeed(self, handle=None, user_did=None, limit=10, cursor=""):
        if handle:
            actor = handle
        elif user_did:
            actor = user_did
        else:
            raise ValueError("Invalid username or did")
        
        request_url = self.ENDPOINTS.getAuthorFeed() + "?actor={}&limit={}&cursor={}".format(actor, limit, cursor)
        response = self.SESSION.get(request_url)
        return response
    
    def getPostThread(self, post_id, limit=10, cursor=""):
        request_url = self.ENDPOINTS.getPostThread() + "?uri={}&limit={}&cursor={}".format(post_id, limit, cursor)
        response = self.SESSION.get(request_url)
        return response

    # app.bsky.graph
    def getFollowers(self, handle=None, user_did=None, limit=10, cursor=""):
        if handle:
            actor = handle
        elif user_did:
            actor = user_did
        else:
            raise ValueError("Invalid username or did")
        
        request_url = self.ENDPOINTS.getFollowers() + "?actor={}&limit={}&cursor={}".format(actor, limit, cursor)
        response = self.SESSION.get(request_url)
        return response
    
    def getFollows(self, handle=None, user_did=None, limit=10, cursor=""):
        if handle:
            actor = handle
        elif user_did:
            actor = user_did
        else:
            raise ValueError("Invalid username or did")
        
        request_url = self.ENDPOINTS.getFollows() + "?actor={}&limit={}&cursor={}".format(actor, limit, cursor)
        response = self.SESSION.get(request_url)
        return response

    # app.bsky.notification
    def listNotifications(self, limit=10, cursor=""):
        request_url = self.ENDPOINTS.listNotifications() + "?limit={}&cursor={}".format(limit, cursor)
        response = self.SESSION.get(request_url)
        return response
    
    def updateSeen(self, limit=10, cursor=""):
        data = { "seenAt": "{}".format(BlueskyHelper.getTimestamp()) }
        request_url = self.ENDPOINTS.updateSeen() + "?limit={}&cursor={}".format(limit, cursor)
        response = self.SESSION.postJson(request_url, json=data)
        return response
    
    # com.atproto.repo
    def createRecord(self, repo, record, collection):
        request_data = {
            "repo": repo,
            "record": record,
            "collection": collection
        }

        response = self.SESSION.postJson(self.ENDPOINTS.createRecord(), json=request_data)
        return response
    
    def deleteRecord(self, repo, record, collection):
        request_data = {
            "repo": repo,
            "record": record,
            "collection": collection
        }

        response = self.SESSION.postJson(self.ENDPOINTS.deleteRecord(), json=request_data)
        return response
    
    def follow(self, handle=None, user_did=None):
        if handle:
            user_did = self.resolveHandle(handle).json().get("did")

        if not user_did or user_did is None:
            raise ValueError("Invalid username")

        follow_request_data = {
            "repo": self.DID,
            "record": {
                "subject": user_did,
                "createdAt": BlueskyHelper.getTimestamp(),
                "$type": "app.bsky.graph.follow"
            },
            "collection": "app.bsky.graph.follow"
        }

        response = self.SESSION.post(self.ENDPOINTS.createRecord(), json=follow_request_data)
        return response
    
    def unfollow(self, handle=None, user_did=None):
        if handle:
            user_did = self.resolveHandle(handle).json().get("did")

        if not user_did or user_did is None:
            raise ValueError("Invalid username")

        unfollow_request_data = {
            "repo": self.DID,
            "record": {
                "subject": user_did,
                "createdAt": BlueskyHelper.getTimestamp(),
                "$type": "app.bsky.graph.unfollow"
            },
            "collection": "app.bsky.graph.unfollow"
        }

        response = self.SESSION.postJson(self.ENDPOINTS.deleteRecord(), json=unfollow_request_data)
        return response

    # com.atproto.identity
    def resolveHandle(self, handle):
        request_url = self.ENDPOINTS.resolveHandle() + "?handle={}".format(handle)
        response = self.SESSION.get(request_url)
        return response
    
    def updateHandle(self, handle):
        request_data = {
            "handle": handle
        }

        response = self.SESSION.postJson(self.ENDPOINTS.updateHandle(), json=request_data)
        return response
