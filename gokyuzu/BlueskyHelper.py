import datetime


class BlueskyHelper:
    def getTimestamp(self):
        return datetime.datetime.now(datetime.timezone.utc).isoformat().replace('+00:00', 'Z')