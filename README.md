# gokyuzu - bluesky python client

Gökyüzü - "sky" in Turkish - is a python client for the [bluesky](https://bsky.social/) social network.

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


#### com.atproto.admin

- `def disableInviteCodes( codes=None, accounts=None)` 
- `def getInviteCodes( sort='recent', limit=100, cursor="")` 
- `def getModerationAction( action_id)` 
- `def getModerationActions( subject=None, limit=10, cursor="")` 
- `def getModerationReport( report_id)` 
- `def getModerationReports( subject=None, resolved=None, limit=10, cursor="")` 
- `def getRecord( uri=None, cid=None)` 
- `def getRepo( user_did)` 
- `def resolveModerationReports( action_id, report_ids, created_by)` 
- `def reverseModerationAction( action_id, reason, created_by)` 
- `def searchRepos( query, limit=10, cursor="")` 
- `def takeModerationAction( action, subject, reason, created_by)` 
- `def updateAccountEmail( account, email)` 
- `def updateAccountHandle( new_handle, handle=None, user_did=None)` 


#### com.atproto.identity

- `def resolveHandle( handle)` 
- `def updateHandle( handle)` 

#### com.atproto.label

- `def queryLabels( uri_patterns, sources=None, limit=10, cursor="")` 
- `def subscribeLabels( cursor="", is_stream=True)` 

#### com.atproto.repo

- `def applyWrites( repo, writes, validate=True, swapCommit=None)` 
- `def createRecord( repo, record, collection, record_key=None, validate=True, swapCommit=None)` 
- `def deleteRecord( repo, record, collection, swapRecord=None, swapCommit=None)` 
- `def describeRepo( repo)` 
- `def getAdminRecord( user_did, collection, record_key, commit=None)` 
- `def listRecords( user_did, collection, limit=10, record_key_start=None, record_key_end=None, reverse=False)` 
- `def putRecord( repo, collection, record_key, record, validate=True, swapRecord=None, swapCommit=None)` 
- `def uploadBlob( blob_bytes)` 
- `def uploadImage( image_path)` 
- `def followRecord( handle=None, user_did=None)` 
- `def unfollowRecord( handle=None, user_did=None)` 

#### com.atproto.server

- `def createAccount( email, handle, password, inviteCode)` 
- `def createAppPassword( name)`
- `def createInviteCode( useCount, user_did=None)` 
- `def createInviteCodes( useCount, codeCount=1, user_did=None)` 
- `def deleteAccount( token, password, handle=None, user_did=None)` 
- `def describeServer()` 
- `def deleteSession()` 
- `def listAppPassword()`
- `def getAccountInviteCodes( limit=10, includeUsed=True, create_available=True)` 
- `def getSession()` 
- `def requestAccountDelete()` 
- `def requestPasswordReset( email)` 
- `def resetPassword( email, password)` 
- `def refreshSession()` 
- `def revokeAppPassword( app_name)`

#### com.atproto.sync

- `def getBlob( repo_did, blob_cid)` 
- `def getBlocks( did, cids)` 
- `def getCheckout( did, commit=None)` 
- `def getCommitPath( did, latest=None, earliest=None)` 
- `def getHead( did)` 
- `def getSyncRecord( did, collection, record_key, commit=None)` 
- `def getRepo( did, earliest=None, latest=None)` 
- `def listBlobs( did, latest, earliest)` 
- `def notifyOfUpdate( hostname)` 
- `def requestCrawl( hostname)` 
- `def subscribeRepos( cursor)` 


#### app.bsky.actor

- `def getProfile( user_did)` 
- `def getProfiles( user_dids)` 
- `def getSuggestions( limit=10, cursor="")` 
- `def searchActors( query, limit=10, cursor="")` 
- `def searchActorsTypeahead( query, limit=10, cursor="")` 


#### app.bsky.feed

- `def getAuthorFeed( handle=None, user_did=None, limit=10, cursor="")` 
- `def getLikes( post_id, limit=10, cursor="")` 
- `def getPostThread( post_id, limit=10, cursor="", depth=None)` 
- `def getRepostedBy( post_id, limit=10, cursor="", post_cid=None)` 
- `def getTimeline( limit=10, cursor="", algorithm="reverse-chronological")` 
- `def like( subject_uri, subject_cid, createdAt=None)` 
- `def unlike( repo, record_key)` 
- `def repost( subject_uri, subject_cid, createdAt=None)` 
- `def undo_repost( repo, record_key)` 


#### app.bsky.graph

- `def follow( handle=None, user_did=None)` 
- `def getFollowers( handle=None, user_did=None, limit=10, cursor="")` 
- `def getFollows( handle=None, user_did=None, limit=10, cursor="")` 
- `def getMutes( limit=10, cursor="")` 
- `def muteActor( handle=None, user_did=None)` 
- `def unmuteActor( handle=None, user_did=None)` 


#### app.bsky.notification

- `def getUnreadCount()` 
- `def listNotifications( limit=10, cursor="")` 
- `def updateSeen( limit=10, cursor="", seenAt=None)` 


#### app.bsky.unspecced

- `def getPopular( limit=10, cursor="")` 


#### app.bsky.richText

- `def facet( text)` 


#### Search sarch.bsky.social

- `def search( query_type="posts", query="")` 
- `def search_profiles( query)` 
- `def search_posts( query)` 

#### Other

- `def health()` 
- `def createLinkFromAtUri( at_uri)`
- `def quote( text, repo, record_uri, record_cid, createdAt=None)` 
- `def delete_post( repo, record_key)` 
- `def comment( text, repo, reply_root_uri, reply_root_cid, reply_parent_uri, reply_parent_cid, createdAt=None)` 


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