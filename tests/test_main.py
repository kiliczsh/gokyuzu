import unittest
from gokyuzu import *

BSKY_SOCIAL_HANDLE = "handle.bsky.social"
BSKY_SOCIAL_PASSWORD = ""

class TestBlueskyLogin(unittest.TestCase):
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
        self.assertIsNotNone(bsky.SESSION)
        self.assertIsNotNone(bsky.SESSION.DID)

        profile = bsky.getProfile(bsky.SESSION.DID)
        self.assertIsNotNone(profile)
        self.assertNotEqual(profile.json().get('did'), '')