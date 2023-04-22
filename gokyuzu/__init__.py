
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

    def resolveHandle(self, username):
        request_url = self.ENDPOINTS.resolveHandle() + "?handle={}".format(username)
        response = self.SESSION.get(request_url)
        return response
    
    def getProfile(self, did):
        request_url = self.ENDPOINTS.getProfile() + "?actor={}".format(did)
        response = self.SESSION.get(request_url)
        return response

    def follow(self, username=None, did_of_user=None):
        if username:
            did_of_user = self.resolveHandle(username).json().get("did")

        if not did_of_user or did_of_user is None:
            raise ValueError("Invalid username")

        follow_request_data = {
            "repo": self.DID,
            "record": {
                "subject": did_of_user,
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
