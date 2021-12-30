import os
from requests_oauthlib import OAuth1Session
from meetmax import session
from meetmax import attendees
from meetmax import events
from meetmax import companies

mm_key = os.getenv("MEETMAX_KEY")
mm_secret = os.getenv("MEETMAX_SECRET")
mm_event_id = 70039

auth = session.create(mm_key, mm_secret)

print(auth)

#Create Companies
all_companies = {
  "event_id" : mm_event_id,
  "search_fld" : "attendee_role_id",
  "search_for" : "NASPO2_SUPPLIER_CO",
  "data_type" : "json"
}

company_data = companies.all(auth, all_companies)

print(company_data)