import requests
import urllib
from requests_oauthlib import OAuth1Session
from requests_oauthlib import OAuth1

#Get Attendees
def all(session, data):
  url = 'https://meetmax.com/sched/service/attendee/list'
  try:
      r = session.get(url, params = data)
      r.raise_for_status()
      return r.json()
    
  except requests.exceptions.HTTPError as e:
      return e.response.json()

#Add Attendees
def add(session, data):
  url = 'https://meetmax.com/sched/service/attendee/add'
  try:
      r = session.get(url, params = data)
      r.raise_for_status()
      return r.json()
    
  except requests.exceptions.HTTPError as e:
      return e.response.json()

def edit(session, data):
  url = 'https://meetmax.com/sched/service/attendee/edit'
  try:
      r = session.get(url, params = data)
      r.raise_for_status()
      return r.json()
    
  except requests.exceptions.HTTPError as e:
      return e.response.json()


