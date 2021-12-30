import requests
from requests_oauthlib import OAuth1Session

#Create Session
def signature(key, secret):
  return OAuth1Session(key,client_secret=secret)

#Get Events - 
def all_events(session, data):
  url = 'https://meetmax.com/sched/service/event/list'
  try:
      r = session.get(url, params = data)
      r.raise_for_status()
      return r.json()
    
  except requests.exceptions.HTTPError as e:
      return e.response.json()

#Get Event Roles
def all_event_roles(session, data):
  url = 'https://meetmax.com/sched/service/attendeerole/list'
  try:
      r = session.get(url, params = data)
      r.raise_for_status()
      return r.json()
    
  except requests.exceptions.HTTPError as e:
      return e.response.json()

#Get Attendees - 
def all_attendees(session, data):
  url = 'https://meetmax.com/sched/service/attendee/list'
  try:
      r = session.get(url, params = data)
      r.raise_for_status()
      return r.json()
    
  except requests.exceptions.HTTPError as e:
      return e.response.json()

#Add Attendees or Company Rep -  
def add_attendee(session, data):
  url = 'https://meetmax.com/sched/service/attendee/add'
  try:
      r = session.get(url, params = data)
      print(r.url)
      r.raise_for_status()
      return r.json()
    
  except requests.exceptions.HTTPError as e:
      return e.response.json()

#Edit Attendee - 
def edit_attendee(session, data):
  url = 'https://meetmax.com/sched/service/attendee/edit'
  try:
      r = session.get(url, params = data)
      r.raise_for_status()
      return r.json()
    
  except requests.exceptions.HTTPError as e:
      return e.response.json()

#Get Companies - Data requires search_fld, and search_for. https://www.meetmax.com/docs/service/company_list.html
def all_companies(session, data):
  url = 'https://meetmax.com/sched/service/attendee/list'
  try:
      r = session.get(url, params = data)
      r.raise_for_status()
      return r.json()
    
  except requests.exceptions.HTTPError as e:
      return e.response.json()

#Add Company - Data requires event_id, first, last, company, attendee_role_id, is_entity, attendee_type, virtual. https://www.meetmax.com/docs/service/company_add.html
def add_company(session, data):
  url = 'https://meetmax.com/sched/service/attendee/add'
  try:
      r = session.get(url, params = data)
      r.raise_for_status()
      return r.json()
    
  except requests.exceptions.HTTPError as e:
      return e.response.json()

#Helper to get number of Industry Category
def industry_number(text):
  options = ["Agricultural Equipment",
  "Automotive/Fleet",
  "Construction Equipment and Supplies Cooperative Purchasing",
  "Equipment Rental and Leasing",
  "Healthcare Supplies",
  "Heavy Machinery",
  "Industrial and Construction",
  "IT Hardware and Software",
  "IT Services",
  "Laboratory Services",
  "Material Goods",
  "Maintenance, Repair and Operations",
  "Mobile Technology",
  "Procurement Services",
  "Professional Services",
  "Sustainable Products",
  "Telecommunications",
  "Other"
  ]

  index = options.index(text)
  return index + 1
