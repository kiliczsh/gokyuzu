import requests

from gokyuzu import BlueskyEndpoints


class BlueskySession():
    def __init__(self, handle, password):
        self.BSKY_SERVER = "https://bsky.social"
        self.DID = ""
        self.HANDLE = handle
        self.EMAIL = ""
        self.ACCESS_TOKEN = ""
        self.REFRESH_TOKEN = ""
        self.ENDPOINTS = BlueskyEndpoints(self.BSKY_SERVER)
        self.createSession(handle, password)

    def __str__(self):
        return f"BlueskySession(handle={self.HANDLE}, email={self.EMAIL}, did={self.DID}, accessToken={self.ACCESS_TOKEN}, refreshToken={self.REFRESH_TOKEN})"

    def createSession(self, handle, password):
        json = {"identifier": handle, "password": password}
        response = self.post(self.ENDPOINTS.createSession(), json=json)
        if response.status_code == 401:
            print("\nIgnore this error if you are running tests.")
            print(response.json())
            return response
        response_body = response.json()
        error = response_body.get('error')
        message = response_body.get('message')
        if error != None:
            print("\nError: {}, Message: {}".format(error, message))
            return response
        self.useResponseBody(response_body)

    def useResponseBody(self, response_body):
        self.DID = response_body.get('did')
        self.HANDLE = response_body.get('handle')
        self.EMAIL = response_body.get('email')
        self.ACCESS_TOKEN = response_body.get('accessJwt')
        self.REFRESH_TOKEN = response_body.get('refreshJwt')

    def getDID(self):
        return self.DID
    
    def getHandle(self):
        return self.HANDLE
    
    def getEmail(self):
        return self.EMAIL
    
    def getAccessToken(self):
        return self.ACCESS_TOKEN
    
    def getRefreshToken(self):
        return self.REFRESH_TOKEN
        
    def get(self, url, **kwargs):
        headers = {'Authorization': f'Bearer {self.getAccessToken()}'}
        response = requests.get(url, headers=headers, **kwargs)
        return response
        
    def post(self, url, data=None, json=None, **kwargs):
        headers = {'Authorization': f'Bearer {self.getAccessToken()}'}
        response = requests.post(url, headers=headers, data=data, json=json, **kwargs)
        return response
