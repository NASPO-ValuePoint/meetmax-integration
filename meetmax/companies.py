import requests

#Get Companies - Data requires search_fld, and search_for. https://www.meetmax.com/docs/service/company_list.html
def all(session, data):
  url = 'https://meetmax.com/sched/service/attendee/list'
  try:
      r = session.get(url, params = data)
      r.raise_for_status()
      return r.json()
    
  except requests.exceptions.HTTPError as e:
      return e.response.json()

#Add Company - Data requires event_id, first, last, company, attendee_role_id, is_entity, attendee_type, virtual. https://www.meetmax.com/docs/service/company_add.html
def add(session, data):
  url = 'https://meetmax.com/sched/service/attendee/add'
  try:
      r = session.get(url, params = data)
      r.raise_for_status()
      return r.json()
    
  except requests.exceptions.HTTPError as e:
      return e.response.json()
