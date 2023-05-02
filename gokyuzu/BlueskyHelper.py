import datetime

from gokyuzu.BlueskyRecords import BlueskyRecords

class BlueskyHelper:
    @classmethod
    def getTimestamp(self):
        return datetime.datetime.now(datetime.timezone.utc).isoformat().replace('+00:00', 'Z')
    
    @classmethod
    def getPostUri(self, user_did, post_id):
        return f"at://{user_did}/{BlueskyRecords.Post}/{post_id}"

    @classmethod
    def createPostLink(self, handle, record_key):
        return f"https://staging.bsky.app/profile/{handle}/post/{record_key}"
    
    @classmethod
    def analyze_at_uri(self, at_uri):
        components = at_uri.split('/')
        did = components[2]
        rkey = components[4]
        return did, rkey