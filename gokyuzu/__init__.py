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