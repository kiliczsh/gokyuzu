# gokyuzu - bluesky python client

Gökyüzü - "sky" in Turkish - is a python client for the [bluesky](bsky.social) social network.

### Install

```bash
pip install gokyuzu
```

### Sample Usage

```python
from gokyuzu import Bluesky

bsky = Bluesky("handle.bsky.social", "PASSWORD")
response = bsky.resolveHandle("handle.bsky.social")
print(response.json())
```

### Documentation

List of Implemented API Calls:

- `createAccount(self, email, handle, password, inviteCode)`
- `getSession(self)`
- `getAccountInviteCodes(self, limit=10)`
- `getProfile(self, user_did)`
- `getProfiles(self, user_dids)`
- `getPopular(self, limit=10, cursor="")`
- `getTimeline(self, limit=10, cursor="", algorithm="reverse-chronological")`
- `getAuthorFeed(self, handle=None, user_did=None, limit=10, cursor="")`
- `getPostThread(self, post_id, limit=10, cursor="")`
- `getFollowers(self, handle=None, user_did=None, limit=10, cursor="")`
- `getFollows(self, handle=None, user_did=None, limit=10, cursor="")`
- `listNotifications(self, limit=10, cursor="")`
- `updateSeen(self, limit=10, cursor="")`
- `createRecord(self, repo, record, collection)`
- `deleteRecord(self, repo, record, collection)`
- `follow(self, handle=None, user_did=None)`
- `unfollow(self, handle=None, user_did=None)`
- `resolveHandle(self, handle)`
- `updateHandle(self, handle)`


### Development

```bash
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### Running tests

```bash
python -m unittest
```

### Publishing to PyPI

```bash
# Build for PyPI
python -m build

# Test PyPI
python -m twine upload --repository testpypi dist/*
pip install --index-url https://test.pypi.org/simple/ --no-deps gokyuzu

# PyPI
python -m twine upload dist/*
pip install gokyuzu
```