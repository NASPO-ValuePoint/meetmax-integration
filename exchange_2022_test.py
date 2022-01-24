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

mm_key = os.getenv("mm_key")
mm_secret = os.getenv("mm_secret")
mm_test_id = 80471

# Get Session
auth = session.create(mm_key, mm_secret)
#print(auth)

conn = psycopg2.connect(host=os.environ.get("DB_HOST"), database=os.environ.get(
    "DB_DATABASE"), user=os.environ.get("DB_USER"), password=os.environ.get("DB_PASSWORD"))
cur = conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor)
# print(cur)

# # Get company data from meetmax
all_companies = {
    "event_id": mm_test_id,
    "search_fld": "attendee_role_id",
    "search_for": "NASPO2_SUPPLIER_CO",
    "data_type": "json"
}
company_mm = companies.all(auth, all_companies)
# print(company_data)
# just get the name of the company from the results
company_map = map(lambda x: x['company'], company_mm['results'])

company_list = list(company_map)
#print(company_list)

# get list of companies from database
query_companies = '''SELECT DISTINCT "Company" FROM warehouse.exchange_meetmax 
                     WHERE attendee_role_id = 'NASPO2_SUPPLIER_ATT'
                     '''
cur.execute(query_companies)
companies_db = cur.fetchall()
# print(companies_db)

for c in companies_db:
    # print(c['Company'])
    if c['Company'] in company_list:
        print(f"Already in meetmax - {c['Company']}")
    else:
        print(f'To be added - {c["Company"]}')
        company_data = {
            "event_id": mm_test_id,
            "first": "Management",
            "last": "Team",
            "company": c['Company'],
            "attendee_role_id": "NASPO2_SUPPLIER_CO",
            "is_entity": "Y",
            "attendee_type": "E",
            "virtual": "Y",
            "data_type": "JSON"
        }
        time.sleep(1)
        added = companies.add(auth, company_data)
        #print(added)

# Get attendee information from warehouse
#query_attendee = '''SELECT * FROM warehouse.exchange_meetmax where meetmax_id is NULL'''
query_attendee = '''SELECT * FROM warehouse.exchange_meetmax where meetmax_id is NULL
                        and "Registration Type" = 'State Member'
                        '''

#Get "Taking 1-on-1 appointments" attendee information from warehouse
query_attendee = '''SELECT * FROM warehouse.exchange_meetmax where meetmax_id is NULL 
                    AND attendee_role_id in ('NASPO2_STATE_REP', 'NASPO2_NASPO_REP') 
                    AND "One-on-One appointments" = 'Yes'
                    '''
cur.execute(query_attendee)
taking_appts = cur.fetchall()
print('Total NASPO2_STATE_REPS to add - ', len(taking_appts))
#print(taking_appts[12])

#add the info to meetmax
for a in taking_appts[:10]:
    #print(a)
    state_rep_att = {
        'event_id': mm_test_id,
        'first': a['First Name'],
        'last': a['Last Name'],
        'company': a['Company'],
        'title': a['Title'],
        'attendee_role_id': 'NASPO2_STATE_REP',
        'email': a['Email'],
        'username': a['Email'],
        'password': 'exchange2022',
        'custom_12784': 'Eastern',
        'custom_12766': a['bio'],
        'custom_7581': a['headshot'],
        'custom_9069': helpers.cleancol(a['Categories/Industries']),
        'custom_14639': a['Status'],
        'receive_request': 'Y' if a['One-on-One appointments'] == 'Yes' else 'N',
        'data_type': 'json'
    }
    #print(state_rep_att)
    time.sleep(1)
    attendee_data = attendees.add(auth, state_rep_att)
    #print(attendee_data)

    if "status_code" in attendee_data:
      cur.execute('''INSERT INTO warehouse.cvent_meetmax(registration_id, meetmax_id)
                        VALUES(%s, %s)''', (a["Registration ID"], attendee_data['id'])
                  )
      print(a["Registration ID"] + " - Attendee Added.")
    else:
      cur.execute('''INSERT INTO warehouse.cvent_meetmax(registration_id, meetmax_status)
                        VALUES(%s, %s)''', (a["Registration ID"], str(attendee_data))
                  )
      print(a["Registration ID"] + " - Error Adding Attendee.")


#Get "Making 1-on-1 appointments attendee information from warehouse
query_attendee = '''SELECT * FROM warehouse.exchange_meetmax
                    WHERE meetmax_id is NULL and
                    "One-on-One appointments" = 'Yes' and
                    "Registration Type" in ('Affiliate Division and Strategic Partners',
                                            'Suppliers',
                                            'Certified Small Business')
                    '''
cur.execute(query_attendee)
making_appts = cur.fetchall()
print('Total NASPO2_SUPPLIER_ATT to add - ', len(making_appts))
#print(making_appts[55])

#add the info to meetmax
for a in making_appts[:15]:
    #print(a)
    suppliers_att = {
        'event_id': mm_test_id,
        'first': a['First Name'],
        'last': a['Last Name'],
        'company': a['Company'],
        'title': a['Title'],
        'attendee_role_id': 'NASPO2_SUPPLIER_ATT',
        'email': a['Email'],
        'username': a['Email'],
        'password': 'exchange2022',
        'custom_12784': 'Eastern',
        'custom_12766': a['bio'],
        'custom_7581': a['headshot'],
        'custom_9069': helpers.cleancol(a['Categories/Industries']),
        'custom_14639': a['Status'],
        'custom_7664': 6,
        'receive_request': 'Y' if a['One-on-One appointments'] == 'Yes' else 'N',
        'data_type': 'json'
    }
    #print(suppliers_att)
    time.sleep(1)
    attendee_data = attendees.add(auth, suppliers_att)
    #print(attendee_data)

    if "status_code" in attendee_data:
      cur.execute('''INSERT INTO warehouse.cvent_meetmax(registration_id, meetmax_id)
                        VALUES(%s, %s)''', (a["Registration ID"], attendee_data['id'])
                  )
      print(a["Registration ID"] + " - Attendee Added.")
    else:
      cur.execute('''INSERT INTO warehouse.cvent_meetmax(registration_id, meetmax_status)
                        VALUES(%s, %s)''', (a["Registration ID"], str(attendee_data))
                  )
      print(a["Registration ID"] + " - Error Adding Attendee.")

conn.commit()
cur.close()
conn.close()
auth.close()

