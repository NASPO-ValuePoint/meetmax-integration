from requests_oauthlib import OAuth1Session

#Create Session
def create(key, secret):
  return OAuth1Session(key,client_secret=secret)