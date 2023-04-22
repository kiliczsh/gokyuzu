import datetime


class BlueskyHelper:
    @classmethod
    def getTimestamp(self):
        return datetime.datetime.now(datetime.timezone.utc).isoformat().replace('+00:00', 'Z')