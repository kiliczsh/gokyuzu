from gokyuzu.BlueskyEndpoints import BlueskyEndpoints
from gokyuzu.BlueskyHelper import BlueskyHelper
from gokyuzu.BlueskyRecords import BlueskyRecords
from gokyuzu.BlueskySession import BlueskySession


class Bluesky():
    def __init__(self, handle, password):
        self.BSKY_SERVER = "https://bsky.social"
        self.ENDPOINTS = BlueskyEndpoints(self.BSKY_SERVER)
        self.SESSION = BlueskySession(handle=handle, password=password)

    def __str__(self):
        return f"Bluesky(server={self.BSKY_SERVER}, handle={self.SESSION.getHandle()}, email={self.SESSION.getEmail()}, did={self.SESSION.getDID()}, accessToken={self.SESSION.getAccessToken()}, refreshToken={self.SESSION.getRefreshToken()})"

    # TODO: Check if admin functions work
    #region com.atproto.admin
    def disableInviteCodes(self, codes=None, accounts=None):
        request_url = self.ENDPOINTS.disableInviteCodes()
        request_data = {
            "codes": codes,
            "accounts": accounts
        }
        response = self.SESSION.postJson(request_url, json=request_data)
        return response
        
    def getInviteCodes(self, sort='recent', limit=100, cursor=""):
        if sort not in ['recent', 'usage']:
            raise ValueError(f"sort must be either 'recent' or 'usage', not '{sort}'")
        
        request_url = self.ENDPOINTS.getInviteCodes() + f"?sort={sort}&limit={limit}&cursor={cursor}"
        response = self.SESSION.get(request_url)
        return response

    def getModerationAction(self, action_id):
        request_url = self.ENDPOINTS.getModerationAction()
        request_data = {
            "id": action_id
        }
        response = self.SESSION.get(request_url, json=request_data)
        return response
    
    def getModerationActions(self, subject=None, limit=10, cursor=""):
        request_url = self.ENDPOINTS.getModerationActions()
        request_data = {
            "subject": subject,
            "limit": limit,
            "cursor": cursor
        }
        response = self.SESSION.get(request_url, json=request_data)
        return response
        
    def getModerationReport(self, report_id):
        request_url = self.ENDPOINTS.getModerationReport()
        request_data = {
            "id": report_id
        }
        response = self.SESSION.get(request_url, json=request_data)
        return response

    def getModerationReports(self, subject=None, resolved=None, limit=10, cursor=""):
        request_url = self.ENDPOINTS.getModerationReports()
        request_data = {
            "subject": subject,
            "resolved": resolved,
            "limit": limit,
            "cursor": cursor
        }
        response = self.SESSION.get(request_url, json=request_data)
        return response
        
    def getAdminRecord(self, uri=None, cid=None):
        request_url = self.ENDPOINTS.getAdminRecord()
        request_data = {}
        if uri is not None:
            request_data['uri'] = uri
        if cid is not None:
            request_data['cid'] = cid
        response = self.SESSION.get(request_url, json=request_data)
        return response
        
    def getRepo(self, user_did):
        request_url = self.ENDPOINTS.getRepo()
        request_data = {
            "did": user_did
        }
        response = self.SESSION.get(request_url, json=request_data)
        return response

    def resolveModerationReports(self, action_id, report_ids, created_by):
        request_url = self.ENDPOINTS.resolveModerationReports()
        request_data = {
            "actionId": action_id,
            "reportIds": report_ids,
            "createdBy": created_by
        }
        response = self.SESSION.postJson(request_url, json=request_data)
        return response
        
    def reverseModerationAction(self, action_id, reason, created_by):
        request_url = self.ENDPOINTS.reverseModerationAction()
        request_data = {
            "id": action_id,
            "reason": reason,
            "createdBy": created_by
        }
        response = self.SESSION.postJson(request_url, json=request_data)
        return response
        
    def searchRepos(self, query, limit=10, cursor=""):
        request_url = self.ENDPOINTS.searchRepos()
        request_data = {
            "term": query,
            "limit": limit,
            "cursor": cursor
        }
        response = self.SESSION.get(request_url, json=request_data)
        return response
        
    def takeModerationAction(self, action, subject, reason, created_by):
        request_url = self.ENDPOINTS.takeModerationAction()
        request_data = {
            "action": action,
            "subject": subject,
            "reason": reason,
            "createdBy": created_by
        }
        response = self.SESSION.postJson(request_url, json=request_data)
        return response
        
    def updateAccountEmail(self, account, email):
        request_url = self.ENDPOINTS.updateAccountEmail()
        request_data = {
            "account": account,
            "email": email
        }
        response = self.SESSION.postJson(request_url, json=request_data)
        return response

    def updateAccountHandle(self, new_handle, handle=None, user_did=None):
        request_url = self.ENDPOINTS.updateAccountHandle()
        if handle:
            did = self.resolveHandle(handle).json()['did']
        elif user_did:
            did = user_did
        else:
            raise ValueError("handle or user_did must be provided")

        request_data = {
            "did": did,
            "handle": new_handle
        }
        response = self.SESSION.postJson(request_url, json=request_data)
        return response
    #endregion

    #region com.atproto.identity
    def resolveHandle(self, handle):
        request_url = self.ENDPOINTS.resolveHandle() + "?handle={}".format(handle)
        response = self.SESSION.get(request_url)
        return response
    
    def updateHandle(self, handle):
        request_url = self.ENDPOINTS.updateHandle()
        request_data = {
            "handle": handle
        }
        response = self.SESSION.postJson(request_url, json=request_data)
        return response
    #endregion

    #region com.atproto.label
    def queryLabels(self, uri_patterns, sources=None, limit=10, cursor=""):
        request_url = self.ENDPOINTS.queryLabels()
        request_data = {
            "uriPatterns": uri_patterns,
            "sources": sources,
            "limit": limit,
            "cursor": cursor
        }
        response = self.SESSION.postJson(request_url, json=request_data)
        return response
    
    def subscribeLabels(self, cursor="", is_stream=True):
        request_url = self.ENDPOINTS.subscribeLabels()
        request_data = {
            "cursor": cursor
        }
        response = self.SESSION.get(request_url, json=request_data, stream=is_stream)
        return response

    #endregion

    #region com.atproto.repo
    def applyWrites(self, repo, writes, validate=True, swapCommit=None):
        request_url = self.ENDPOINTS.applyWrites()
        request_data = {
            "repo": repo,
            "validate": validate,
            "writes": writes,
            "swapCommit": swapCommit
        }
        response = self.SESSION.postJson(request_url, json=request_data)
        return response

    def createRecord(self, repo, record, collection, record_key=None, validate=True, swapCommit=None):
        request_url = self.ENDPOINTS.createRecord()
        request_data = {
            "repo": repo,
            "record": record,
            "collection": collection,
            "validate": validate
        }
        if record_key is not None:
            request_data["recordKey"] = record_key
        
        if swapCommit is not None:
            request_data["swapCommit"] = swapCommit

        response = self.SESSION.postJson(request_url, json=request_data)
        return response
    
    def deleteRecord(self, repo, record, collection, swapRecord=None, swapCommit=None):
        request_url = self.ENDPOINTS.deleteRecord()
        # TODO: rkey or record? 
        request_data = {
            "repo": repo,
            "record": record,
            "collection": collection,
            "swapRecord": swapRecord,
            "swapCommit": swapCommit
        }
        response = self.SESSION.postJson(request_url, json=request_data)
        return response
    
    def describeRepo(self, repo):
        request_url = self.ENDPOINTS.describeRepo()
        request_data = {
            "repo": repo
        }
        response = self.SESSION.postJson(request_url, json=request_data)
        return response

    def getRecord(self, user_did, collection, record_key, commit=None):
        request_url = self.ENDPOINTS.getRecord() + "?repo={}&collection={}&rkey={}".format(user_did, collection, record_key)
        if commit is not None:
            request_url += "&commit={}".format(commit)
        response = self.SESSION.get(request_url)
        return response

    def listRecords(self, user_did, collection, limit=10, record_key_start=None, record_key_end=None, reverse=False):
        request_url = self.ENDPOINTS.listRecords()
        request_data = {
            "repo": user_did,
            "collection": collection,
            "limit": limit,
            "rkeyStart": record_key_start,
            "rkeyEnd": record_key_end,
            "reverse": reverse
        }
        response = self.SESSION.postJson(request_url, json=request_data)
        return response
    
    def putRecord(self, repo, collection, record_key, record, validate=True, swapRecord=None, swapCommit=None):
        request_url = self.ENDPOINTS.putRecord()
        request_data = {
            "repo": repo,
            "collection": collection,
            "rkey": record_key,
            "validate": validate,
            "record": record,
            "swapRecord": swapRecord,
            "swapCommit": swapCommit
        }
        response = self.SESSION.postJson(request_url, json=request_data)
        return response

    def uploadBlob(self, blob_bytes):
        request_url = self.ENDPOINTS.uploadBlob()
        response = self.SESSION.postJson(request_url, json=blob_bytes)
        return response

    def uploadImage(self, image_path):
        request_url = self.ENDPOINTS.uploadBlob()
        with open(image_path, 'rb') as f:
            jpeg = f.read()
            response = self.SESSION.postJpeg(request_url, jpeg=jpeg)
        return response

    def followRecord(self, handle=None, user_did=None):
        request_url = self.ENDPOINTS.createRecord()
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

        response = self.SESSION.post(request_url, json=follow_request_data)
        return response
    
    def unfollowRecord(self, handle=None, user_did=None):
        request_url = self.ENDPOINTS.deleteRecord()
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

        response = self.SESSION.postJson(request_url, json=unfollow_request_data)
        return response
    #endregion

    #region com.atproto.server
    def createAccount(self, email, handle, password, inviteCode):
        request_url = self.ENDPOINTS.createAccount()
        request_data = {
            "email": email,
            "handle": handle,
            "password": password,
            "inviteCode": inviteCode
        }

        response = self.SESSION.postJson(request_url, json=request_data)
        return response
    
    def createAppPassword(self, app_name):
        request_url = self.ENDPOINTS.createAppPassword()
        request_data = {
            "name": app_name
        }
        response = self.SESSION.postJson(request_url, json=request_data)
        return response

    def createInviteCode(self, useCount, user_did=None):
        request_url = self.ENDPOINTS.createInviteCode()
        if user_did is None:
            user_did = self.SESSION.getDID()

        request_data = {
            "useCount": useCount,
            "forAccount": user_did
        }
        response = self.SESSION.postJson(request_url, json=request_data)
        return response
    
    def createInviteCodes(self, useCount, codeCount=1, user_did=None):
        request_url = self.ENDPOINTS.createInviteCodes()
        if user_did is None:
            user_did = self.SESSION.getDID()

        request_data = {
            "useCount": useCount,
            "forAccount": user_did,
            "codeCount": codeCount
        }
        response = self.SESSION.postJson(request_url, json=request_data)
        return response

    def deleteAccount(self, token, password, handle=None, user_did=None):
        if handle:
            user_did = self.resolveHandle(handle)
        elif user_did is None:
            user_did = self.SESSION.getDID()

        request_url = self.ENDPOINTS.deleteAccount()
        request_data = {
            "did": user_did,
            "password": password,
            "token": token
        }
        response = self.SESSION.postJson(request_url, json=request_data)
        return response
    
    def describeServer(self):
        request_url = self.ENDPOINTS.describeServer()
        response = self.SESSION.get(request_url)
        return response

    def deleteSession(self):
        request_url = self.ENDPOINTS.deleteSession()
        response = self.SESSION.post(request_url)
        return response
    
    def getAccountInviteCodes(self, limit=10, includeUsed=True, create_available=True):
        request_url = self.ENDPOINTS.getAccountInviteCodes() + "?limit={}&includeUsed={}&create_available={}".format(limit, includeUsed, create_available)
        response = self.SESSION.get(request_url)
        return response
    
    def getSession(self):
        request_url = self.ENDPOINTS.getSession()
        response = self.SESSION.get(request_url)
        return response

    def listAppPasswords(self):
        request_url = self.ENDPOINTS.listAppPasswords()
        response = self.SESSION.get(request_url)
        return response
    
    def requestAccountDelete(self):
        request_url = self.ENDPOINTS.requestAccountDelete()
        response = self.SESSION.post(request_url)
        return response

    def requestPasswordReset(self, email):
        request_url = self.ENDPOINTS.requestPasswordReset()
        request_data = {
            "email": email
        }
        response = self.SESSION.postJson(request_url, json=request_data)
        return response
    
    def resetPassword(self, email, password):
        request_url = self.ENDPOINTS.resetPassword()
        request_data = {
            "email": email,
            "password": password
        }
        response = self.SESSION.postJson(request_url, json=request_data)
        return response

    def refreshSession(self):
        request_url = self.ENDPOINTS.refreshSession()
        request_data = {
            "refresh_token": self.SESSION.getRefreshToken()
        } 
        response = self.SESSION.postJson(request_url, json=request_data)
        self.SESSION.useResponseBody(response.content)
        return response

    def revokeAppPassword(self, app_name):
        request_url = self.ENDPOINTS.revokeAppPassword()
        request_data = {
            "name": app_name
        }
        response = self.SESSION.postJson(request_url, json=request_data)
        return response

    #endregion

    #region com.atproto.sync
    def getBlob(self, repo_did, blob_cid):
        request_url = self.ENDPOINTS.getBlob() + "?did={}&cid={}".format(repo_did, blob_cid)
        response = self.SESSION.get(request_url)
        return response
    
    def getBlocks(self, did, cids):
        request_url = self.ENDPOINTS.getBlocks() + "?did={}&cids={}".format(did, cids)
        response = self.SESSION.get(request_url)
        return response

    def getCheckout(self, did, commit=None):
        request_url = self.ENDPOINTS.getCheckout() 
        request_data = {
            "did": did
        }
        if commit:
            request_data["commit"] = commit
        
        response = self.SESSION.postJson(request_url, json=request_data)
        return response
    
    def getCommitPath(self, did, latest=None, earliest=None):
        request_url = self.ENDPOINTS.getCommitPath()
        request_data = {
            "did": did
        }
        if latest:
            request_data["latest"] = latest
        if earliest:
            request_data["earliest"] = earliest

        response = self.SESSION.postJson(request_url, json=request_data)
        return response

    def getHead(self, did):
        request_url = self.ENDPOINTS.getHead() + "?did={}".format(did)
        response = self.SESSION.get(request_url)
        return response

    def getSyncRecord(self, did, collection, record_key, commit=None):
        request_url = self.ENDPOINTS.getSyncRecord()
        request_data = {
            "did": did,
            "collection": collection,
            "key": record_key
        }
        if commit:
            request_data["commit"] = commit
        
        response = self.SESSION.postJson(request_url, json=request_data)
        return response

    def getRepo(self, did, earliest=None, latest=None):
        if earliest is not None and latest is not None:
            request_url = self.ENDPOINTS.getRepo() + "?did={}&earliest={}&latest={}".format(did, earliest, latest)
        elif earliest is not None:
            request_url = self.ENDPOINTS.getRepo() + "?did={}&earliest={}".format(did, earliest)
        elif latest is not None:
            request_url = self.ENDPOINTS.getRepo() + "?did={}&latest={}".format(did, latest)
        else:
            request_url = self.ENDPOINTS.getRepo() + "?did={}".format(did)
        response = self.SESSION.get(request_url)
        return response
    
    def listBlobs(self, did, latest, earliest):
        request_url = self.ENDPOINTS.listBlobs()
        request_data = {
            "did": did,
            "latest": latest,
            "earliest": earliest
        }
        response = self.SESSION.postJson(request_url, json=request_data)
        return response

    def notifyOfUpdate(self, hostname):
        request_url = self.ENDPOINTS.notifyOfUpdate()
        request_data = {
            "hostname": hostname
        }
        response = self.SESSION.postJson(request_url, json=request_data)
        return response
    
    def requestCrawl(self, hostname):
        request_url = self.ENDPOINTS.requestCrawl()
        request_data = {
            "hostname": hostname
        }
        response = self.SESSION.postJson(request_url, json=request_data)
        return response
    
    def subscribeRepos(self, cursor):
        request_url = self.ENDPOINTS.subscribeRepos() + "?cursor={}".format(cursor)
        response = self.SESSION.get(request_url)
        return response

    #endregion

    #region app.bsky.actor
    def getProfile(self, user_did):
        request_url = self.ENDPOINTS.getProfile() + "?actor={}".format(user_did)
        response = self.SESSION.get(request_url)
        return response
    
    def getProfiles(self, user_dids):
        request_url = self.ENDPOINTS.getProfiles() + "?actors={}".format(user_dids)
        response = self.SESSION.get(request_url)
        return response
    
    def getSuggestions(self, limit=10, cursor=""):
        request_url = self.ENDPOINTS.getSuggestions() + "?limit={}&cursor={}".format(limit, cursor)
        response = self.SESSION.get(request_url)
        return response

    def searchActors(self, query, limit=10, cursor=""):
        request_url = self.ENDPOINTS.searchActors() + "?term={}&limit={}&cursor={}".format(query, limit, cursor)
        response = self.SESSION.get(request_url)
        return response
    
    def searchActorsTypeahead(self, query, limit=10, cursor=""):
        request_url = self.ENDPOINTS.searchActorsTypeahead() + "?term={}&limit={}&cursor={}".format(query, limit, cursor)
        response = self.SESSION.get(request_url)
        return response

    #endregion

    #region app.bsky.feed
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
    
    def getLikes(self, post_id, limit=10, cursor=""):
        request_url = self.ENDPOINTS.getLikes() + "?uri={}&limit={}&cursor={}".format(post_id, limit, cursor)
        response = self.SESSION.get(request_url)
        return response
    
    def getPostThread(self, post_id, limit=10, cursor="", depth=None):
        request_url = self.ENDPOINTS.getPostThread() + "?uri={}&limit={}&cursor={}".format(post_id, limit, cursor)
        if depth:
            request_url += "&depth={}".format(depth)

        response = self.SESSION.get(request_url)
        return response

    def getRepostedBy(self, post_id, limit=10, cursor="", post_cid=None):
        request_url = self.ENDPOINTS.getRepostedBy() + "?uri={}&limit={}&cursor={}".format(post_id, limit, cursor)
        if post_cid:
            request_url += "&cid={}".format(post_cid)
        response = self.SESSION.get(request_url)
        return response
    
    def getTimeline(self, limit=10, cursor="", algorithm="reverse-chronological"):
        request_url = self.ENDPOINTS.getTimeline() + "?algorithm={}&limit={}&cursor={}".format(algorithm, limit, cursor)
        response = self.SESSION.get(request_url)
        return response
    
    def like(self, subject_uri, subject_cid, createdAt=None):
        if createdAt is None:
            createdAt = BlueskyHelper.getTimestamp()

        request_data = {
            "collection": BlueskyRecords.Like,
            "$type": BlueskyRecords.Like,
            "repo": self.SESSION.getDID(),
            "record": {
                "subject": {
                    "uri": subject_uri,
                    "cid": subject_cid
                },
                "createdAt": createdAt,
                "$type": BlueskyRecords.Like
            }
        }

        response = self.SESSION.createRecord(request_data=request_data)
        return response
    
    def unlike(self, repo, record_key):
        request_data = {
            "collection": BlueskyRecords.Like,
            "repo": repo,
            "rkey": record_key
        }
        response = self.SESSION.deleteRecord(request_data=request_data)
        return response
    
    def repost(self, subject_uri, subject_cid, createdAt=None):
        if createdAt is None:
            createdAt = BlueskyHelper.getTimestamp()

        request_data = {
            "collection": BlueskyRecords.Repost,
            "$type": BlueskyRecords.Repost,
            "repo": self.SESSION.getDID(),
            "record": {
                "subject": {
                    "uri": subject_uri,
                    "cid": subject_cid
                },
                "createdAt": createdAt,
                "$type": BlueskyRecords.Repost
            }
        }
        
        response = self.SESSION.createRecord(request_data=request_data)
        return response

    def undo_repost(self, repo, record_key):
        request_data = {
            "collection": BlueskyRecords.Repost,
            "repo": repo,
            "rkey": record_key
        }
        response = self.SESSION.deleteRecord(request_data=request_data)
        return response

    #endregion

    #region app.bsky.graph
    def follow(self, handle=None, user_did=None):
        if handle:
            subject = handle
        elif user_did:
            subject = user_did
        else:
            raise ValueError("Invalid username or did")
        
        request_url = self.ENDPOINTS.follow()
        request_data = {
            "subject": subject
        }
        response = self.SESSION.postJson(request_url, json=request_data)
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
    
    def getMutes(self, limit=10, cursor=""):
        request_url = self.ENDPOINTS.getMutes() + "?limit={}&cursor={}".format(limit, cursor)
        response = self.SESSION.get(request_url)
        return response

    def muteActor(self, handle=None, user_did=None):
        if handle:
            actor = handle
        elif user_did:
            actor = user_did
        else:
            raise ValueError("Invalid username or did")
        
        request_url = self.ENDPOINTS.muteActor()
        request_data = {
            "actor": actor
        }
        response = self.SESSION.postJson(request_url, json=request_data)
        return response
    
    def unmuteActor(self, handle=None, user_did=None):
        if handle:
            actor = handle
        elif user_did:
            actor = user_did
        else:
            raise ValueError("Invalid username or did")
        
        request_url = self.ENDPOINTS.unmuteActor()
        request_data = {
            "actor": actor
        }
        response = self.SESSION.postJson(request_url, json=request_data)
        return response
    
    #endregion

    #region app.bsky.notification
    def getUnreadCount(self):
        request_url = self.ENDPOINTS.getUnreadCount()
        response = self.SESSION.get(request_url)
        return response

    def listNotifications(self, limit=10, cursor=""):
        request_url = self.ENDPOINTS.listNotifications() + "?limit={}&cursor={}".format(limit, cursor)
        response = self.SESSION.get(request_url)
        return response
    
    def updateSeen(self, limit=10, cursor="", seenAt=None):
        if seenAt:
            request_data = { "seenAt": seenAt }
        else:
            request_data = { "seenAt": "{}".format(BlueskyHelper.getTimestamp()) }
        request_url = self.ENDPOINTS.updateSeen() + "?limit={}&cursor={}".format(limit, cursor)
        response = self.SESSION.postJson(request_url, json=request_data)
        return response
    #endregion

    #region app.bsky.unspecced
    def getPopular(self, limit=10, cursor=""):
        request_url = self.ENDPOINTS.getPopular() + "?limit={}&cursor={}".format(limit, cursor)
        response = self.SESSION.get(request_url)
        return response
    #endregion

    #region app.bsky.richText
    def facet(self, text):
        request_url = self.ENDPOINTS.facet()
        request_data = {
            "text": text
        }
        response = self.SESSION.postJson(request_url, json=request_data)
        return response

    #endregion

    #region unspecced
    def health(self):
        request_url = self.ENDPOINTS.health()
        response = self.SESSION.get(request_url)
        return response
    
    def createLinkFromAtUri(self, at_uri):
        did, rkey = BlueskyHelper.analyze_at_uri(at_uri)
        handle = self.getProfile(did).json().get("handle")
        return BlueskyHelper.createPostLink(handle, rkey)

    def quote(self, text, repo, record_uri, record_cid, createdAt=None):
        if createdAt is None:
            createdAt = BlueskyHelper.getTimestamp()

        request_data = {
            "collection": str(BlueskyRecords.Post),
            "repo": repo,
            "record":{
                "text": text,
                "embed":{
                "$type": str(BlueskyRecords.EmbedRecord),
                "record":{
                    "uri": record_uri,
                    "cid": record_cid
                }
                },
                "createdAt": createdAt,
                "$type": str(BlueskyRecords.Post)
            }
        }
        response = self.SESSION.createRecord(request_data=request_data)
        return response

    def delete_post(self, repo, record_key):
        request_data = {
            "collection": str(BlueskyRecords.Post),
            "repo": repo,
            "rkey": record_key
        }
        response = self.SESSION.deleteRecord(request_data=request_data)
        return response

    # TODO: simplify comment function
    def comment(self, text, repo, reply_root_uri, reply_root_cid, reply_parent_uri, reply_parent_cid, createdAt=None):
        if createdAt is None:
            createdAt = BlueskyHelper.getTimestamp()

        request_data = {
            "collection": str(BlueskyRecords.Post),
            "repo": repo,
            "record":{
                "text":text,
                "reply":{
                    "root":{
                        "uri": reply_root_uri,
                        "cid": reply_root_cid
                    },
                    "parent":{
                        "uri": reply_parent_uri,
                        "cid": reply_parent_cid
                    }
                },
                "createdAt": createdAt,
                "$type": str(BlueskyRecords.Post)
            }
        }
        response = self.SESSION.createRecord(request_data=request_data)
        return response
    
    #endregion

    #region Search sarch.bsky.social
    def search(self, query_type="posts", query=""):
        request_url = "https://search.bsky.social/search/{}?q={}".format(query_type, query)
        response = self.SESSION.get(request_url)
        return response

    def search_profiles(self, query):
        return self.search(query_type="profiles", query=query)
    
    def search_posts(self, query):
        return self.search(query_type="posts", query=query)
    #endregion
