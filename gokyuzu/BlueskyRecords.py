from enum import Enum

class BlueskyRecords(Enum):
    def __str__(self):
        return str(self.value)

    Like = "app.bsky.feed.like"
    Post = "app.bsky.feed.post"
    Repost = "app.bsky.feed.repost"
    EmbedRecord = "app.bsky.embed.record"