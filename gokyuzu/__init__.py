
import json
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

    def resolveHandle(self, handle):
        request_url = self.ENDPOINTS.resolveHandle() + "?handle={}".format(handle)
        response = self.SESSION.get(request_url)
        return response
    
    def getProfile(self, user_did):
        request_url = self.ENDPOINTS.getProfile() + "?actor={}".format(user_did)
        response = self.SESSION.get(request_url)
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

    def getAccountInviteCodes(self, limit=10):
        request_url = self.ENDPOINTS.getAccountInviteCodes() + "?limit={}".format(limit)
        response = self.SESSION.get(request_url)
        return response
    
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
    
    def listNotifications(self, limit=10, cursor=""):
        request_url = self.ENDPOINTS.listNotifications() + "?limit={}&cursor={}".format(limit, cursor)
        response = self.SESSION.get(request_url)
        return response
    
    def updateSeen(self, limit=10, cursor=""):
        data = { "seenAt": "{}".format(BlueskyHelper.getTimestamp()) }
        request_url = self.ENDPOINTS.updateSeen() + "?limit={}&cursor={}".format(limit, cursor)
        response = self.SESSION.postJson(request_url, json=data)
        return response
    
    def getTimeline(self, limit=10, cursor="", algorithm="reverse-chronological"):
        request_url = self.ENDPOINTS.getTimeline() + "?algorithm={}&limit={}&cursor={}".format(algorithm, limit, cursor)
        response = self.SESSION.get(request_url)
        return response
