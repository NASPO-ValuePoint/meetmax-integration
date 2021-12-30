import os
import time
import json
import uuid
import urllib
import requests
import psycopg2
import psycopg2.extras
import oauthlib
from requests_oauthlib import OAuth1Session
from meetmax import session
from meetmax import events
from meetmax import companies
from meetmax import attendees
from meetmax import helpers
from dotenv import load_dotenv
load_dotenv()

mm_key = os.getenv("MEETMAX_KEY")
mm_secret = os.getenv("MEETMAX_SECRET")
mm_event_id = 70039

# Get Session
auth = session.create(mm_key, mm_secret)

conn = psycopg2.connect(host=os.environ.get("DB_HOST"), database=os.environ.get(
        "DB_DATABASE"), user=os.environ.get("DB_USER"), password=os.environ.get("DB_PASSWORD"))
cur = conn.cursor(cursor_factory = psycopg2.extras.RealDictCursor)

#Create Companies
all_companies = {
  "event_id" : mm_event_id,
  "search_fld" : "attendee_role_id",
  "search_for" : "NASPO2_SUPPLIER_CO",
  "data_type" : "json"
}

company_data = companies.all(auth, all_companies)

company_map = map(lambda x: x['company'], company_data['results']) 

company_list = list(company_map)

companies_q = "SELECT DISTINCT company FROM conferences_events.exchange_meetmax WHERE attendee_role_id = 'NASPO2_SUPPLIER_ATT'"
cur.execute(companies_q)
res_c = cur.fetchall()

for x in res_c:
  
  if x["company"] in company_list:
    print(x["company"] + ' already exists.')
  
  else:
    time.sleep(1)
    company = {
    "event_id" : mm_event_id,
    "first" : "Management",
    "last" : "Team",
    "company" : x["company"],
    "attendee_role_id" : "NASPO2_SUPPLIER_CO",
    "is_entity" : "Y",
    "attendee_type" : "E",
    "virtual" : "Y",
    "data_type" : "json"
    }
    mm_company = companies.add(auth, company)
    print(x["company"])
    print(mm_company)
# End Create Companies   

#Get Registrations
registrations = 'SELECT * FROM conferences_events.exchange_meetmax WHERE meetmax_id IS NULL and id <> 9652603;'

cur.execute(registrations)
res = cur.fetchall()
for x in res:
  
  #Wait for One Sec Between Records
  time.sleep(1)
  #Suppliers
  if x["attendee_role_id"] == 'NASPO2_SUPPLIER_ATT':
    company_rep = {
    'event_id' : mm_event_id,
    'crm_id' : x["registration_id"],
    'first' : x["first_name"], 
    'last' : x["last_name"], 
    'company' : x["company"],
    'title' : x["title"],
    'telephone' : x["phone"],
    'attendee_role_id' : x["attendee_role_id"],
    'email' : x["email"],
    'username' : x["email"],
    'password' : 'exchange2021',
    'custom_12766' : x["profile"],
    'custom_12784' : x["locale"],
    'grp_name' : x["group_name"],
    'receive_request' : x["receive_request"],
    'custom_7581' : x["headshot"],
    'custom_8928' : x["other_industries"],
    'custom_9069' : x["industries"],
    'custom_7664' : x["meetings"],
    'is_contact' : 'Y',
    'data_type' : 'json'
    }

    mm_co_record = attendees.add(auth, company_rep)
    
    if "status_code" in mm_co_record:
      cur.execute("UPDATE conferences_events.exchange_registration SET meetmax_id = %s WHERE id = %s", (mm_co_record["id"],x["id"]))
      print(x["registration_id"] + " - Attendee Added.")
    else:
      cur.execute("UPDATE conferences_events.exchange_registration SET meetmax_status = %s WHERE id = %s", (str(mm_co_record),x["id"]))
      print(x["registration_id"] + " - Error Adding Attendee.")
  
  #State Members and Others
  else: 
    attendee = {
    'event_id' : mm_event_id,
    'crm_id' : x["registration_id"],
    'first' : x["first_name"], 
    'last' : x["last_name"], 
    'company' : x["company"],
    'title' : x["title"],
    'telephone' : x["phone"],
    'attendee_role_id' : x["attendee_role_id"],
    'email' : x["email"],
    'username' : x["email"],
    'password' : 'exchange2021',
    'custom_12766' : x["profile"],
    'custom_12784' : x["locale"],
    'grp_name' : x["group_name"],
    'receive_request' : x["receive_request"],
    'custom_7581' : x["headshot"],
    'custom_8928' : x["other_industries"],
    'custom_9069' : x["industries"],
    'data_type' : 'json'
    }

    mm_record = attendees.add(auth, attendee)
    
    if "status_code" in mm_record:
      cur.execute("UPDATE conferences_events.exchange_registration SET meetmax_id = %s WHERE id = %s", (mm_record["id"],x["id"]))
      print(x["registration_id"] + " - Attendee Added.")
    else:
      cur.execute("UPDATE conferences_events.exchange_registration SET meetmax_status = %s WHERE id = %s", (str(mm_record),x["id"]))
      print(x["registration_id"] + " - Error Adding Attendee.")
    
  conn.commit()

cur.close()
conn.close()
