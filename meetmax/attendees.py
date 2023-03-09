import requests
import time
from meetmax import helpers
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

#Add Supplier Attendees
def add_supplier(session, record, event_id):
  url = 'https://meetmax.com/sched/service/attendee/add'
  suppliers_att = {
      'event_id': event_id,
      'first': record['First Name'],
      'last': record['Last Name'],
      'company': record['Company'],
      'title': record['Title'],
      'attendee_role_id': 'NASPO2_SUPPLIER_ATT',
      'email': record['Email'],
      'username': record['Email'],
      'password': 'exchange2023',
      #'custom_12784': 'Eastern', Not needed, this is only for virtual events
      'custom_12766': record['bio'],
      'custom_7581': record['headshot'],
      'custom_9069': helpers.cleancol(record['Categories/Industries'])[0],
      'custom_8928': helpers.cleancol(record['Categories/Industries'])[1],
      'custom_14639': record['Status'],
      'custom_7664': 6,
      'receive_request': 'Y' if record['One-on-One appointments'] == 'Yes' else 'N',
      'data_type': 'json'
  }
  # print(suppliers_att)
  time.sleep(2)
  try:
      r = session.get(url, params = suppliers_att)
      r.raise_for_status()
      return r.json()
    
  except requests.exceptions.HTTPError as e:
      return e.response.json()


# Add Attendees
def add_statemember(session, record, event_id):
    url = 'https://meetmax.com/sched/service/attendee/add'
    state_rep_att = {
        'event_id': event_id,
        'first': record['First Name'],
        'last': record['Last Name'],
        'company': record['Company'],
        'title': record['Title'],
        'attendee_role_id': 'NASPO2_STATE_REP',
        'email': record['Email'],
        'username': record['Email'],
        'password': 'exchange2023',
        #'custom_12784': 'Eastern',
        'custom_12766': record['bio'],
        'custom_7581': record['headshot'],
        'custom_9069': helpers.cleancol(record['Categories/Industries'])[0],
        'custom_8928': helpers.cleancol(record['Categories/Industries'])[1],
        'custom_14639': record['Status'],
        'receive_request': 'Y' if record['One-on-One appointments'] == 'Yes' else 'N',
        'data_type': 'json'
    }
    # print(state_rep_att)
    time.sleep(2)
    try:
        r = session.get(url, params=state_rep_att)
        r.raise_for_status()
        return r.json()

    except requests.exceptions.HTTPError as e:
        return e.response.json()

def add_other(session, record, event_id):
    url = 'https://meetmax.com/sched/service/attendee/add'
    others = {
        'event_id': event_id,
        'first': record['First Name'],
        'last': record['Last Name'],
        'company': record['Company'],
        'title': record['Title'],
        'attendee_role_id': 'NASPO2_OTHER_ATTENDEE',
        'email': record['Email'],
        'username': record['Email'],
        'password': 'exchange2023',
        #'custom_12784': 'Eastern',
        'custom_12766': record['bio'],
        'custom_7581': record['headshot'],
        'custom_14639': record['Status'],
        'receive_request': 'N',
        'data_type': 'json'
    }
    # print(state_rep_att)
    time.sleep(2)
    try:
        r = session.get(url, params=others)
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


