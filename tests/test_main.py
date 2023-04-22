import unittest
import os
from gokyuzu import *

BSKY_SOCIAL_HANDLE = str(os.environ.get('BSKY_SOCIAL_HANDLE'))
BSKY_SOCIAL_PASSWORD = str(os.environ.get('BSKY_SOCIAL_PASSWORD'))

class TestBluesky(unittest.TestCase):
    def test_env(self):
        self.assertNotEqual(BSKY_SOCIAL_HANDLE, '')
        self.assertNotEqual(BSKY_SOCIAL_PASSWORD, '')

    def test_login(self):
        bsky = Bluesky(BSKY_SOCIAL_HANDLE, BSKY_SOCIAL_PASSWORD)
        self.assertIsNotNone(bsky.SESSION)
        self.assertIsNotNone(bsky.SESSION.DID)
        self.assertIsNotNone(bsky.SESSION.ACCESS_TOKEN)
        self.assertNotEqual(bsky.SESSION.ACCESS_TOKEN, '') 
        self.assertIsNotNone(bsky.SESSION.REFRESH_TOKEN)
        self.assertIsNotNone(bsky.SESSION.EMAIL)

    def test_login_401(self):
        bsky = Bluesky("dummy","password")
        self.assertEqual(bsky.SESSION.DID, '')
        self.assertEqual(bsky.SESSION.ACCESS_TOKEN, '')

    def test_getProfile(self):
        bsky = Bluesky(BSKY_SOCIAL_HANDLE, BSKY_SOCIAL_PASSWORD)
        profile = bsky.getProfile(bsky.SESSION.DID)
        self.assertIsNotNone(profile)
        self.assertNotEqual(profile.json().get('did'), '')

    def test_invitationCodes(self):
        bsky = Bluesky(BSKY_SOCIAL_HANDLE, BSKY_SOCIAL_PASSWORD)
        invitationCodes = bsky.getAccountInviteCodes()
        self.assertIsNotNone(invitationCodes)
        self.assertNotEqual(invitationCodes.json().get('codes'), '')
        self.assertNotEqual(invitationCodes.json().get('codes'), None)
        print(f"Invitation codes count: {len(invitationCodes.json().get('codes'))}")

    def test_getFollowers_by_username(self):
        bsky = Bluesky(BSKY_SOCIAL_HANDLE, BSKY_SOCIAL_PASSWORD)
        followers = bsky.getFollowers(bsky.SESSION.HANDLE)
        self.assertIsNotNone(followers)
        self.assertNotEqual(followers.json().get('followers'), '')
        self.assertNotEqual(followers.json().get('followers'), None)
        print(f"Followers count: {len(followers.json().get('followers'))}")

    def test_getFollowers_by_did(self):
        bsky = Bluesky(BSKY_SOCIAL_HANDLE, BSKY_SOCIAL_PASSWORD)
        followers = bsky.getFollowers(user_did=bsky.SESSION.DID)
        self.assertIsNotNone(followers)
        self.assertNotEqual(followers.json().get('followers'), '')
        self.assertNotEqual(followers.json().get('followers'), None)
        print(f"Followers count: {len(followers.json().get('followers'))}")

    def test_getFollows_by_username(self):
        bsky = Bluesky(BSKY_SOCIAL_HANDLE, BSKY_SOCIAL_PASSWORD)
        follows = bsky.getFollows(bsky.SESSION.HANDLE)
        self.assertIsNotNone(follows)
        self.assertNotEqual(follows.json().get('follows'), '')
        self.assertNotEqual(follows.json().get('follows'), None)
        print(f"Follows count: {len(follows.json().get('follows'))}")
    
    def test_getFollows_by_did(self):
        bsky = Bluesky(BSKY_SOCIAL_HANDLE, BSKY_SOCIAL_PASSWORD)
        follows = bsky.getFollows(user_did=bsky.SESSION.DID)
        self.assertIsNotNone(follows)
        self.assertNotEqual(follows.json().get('follows'), '')
        self.assertNotEqual(follows.json().get('follows'), None)
        print(f"Follows count: {len(follows.json().get('follows'))}")

    def test_listNotifications(self):
        bsky = Bluesky(BSKY_SOCIAL_HANDLE, BSKY_SOCIAL_PASSWORD)
        notifications = bsky.listNotifications()
        self.assertIsNotNone(notifications)
        self.assertNotEqual(notifications.json().get('notifications'), '')
        self.assertNotEqual(notifications.json().get('notifications'), None)
        print(f"Notifications count: {len(notifications.json().get('notifications'))}")

    def test_updateSeen(self):
        bsky = Bluesky(BSKY_SOCIAL_HANDLE, BSKY_SOCIAL_PASSWORD)
        updateSeenAt = bsky.updateSeen()
        print(updateSeenAt.status_code)
        print(updateSeenAt.content)
        self.assertIsNotNone(updateSeenAt)
