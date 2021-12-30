import os
import time
import json
import urllib
import requests
from requests_oauthlib import OAuth1Session
import session
import events
import companies
import attendees
from dotenv import load_dotenv
load_dotenv()

mm_key = os.getenv("MEETMAX_KEY")
mm_secret = os.getenv("MEETMAX_SECRET")

auth = session.create(mm_key, mm_secret)

eventData = {
  "data_type" : "JSON"
}

eventRoles = {
  "event_id" : 71011,
  "data_type" : "JSON"
}

companyData = {
  "event_id" : 71011,
  "search_fld" : "attendee_role_id",
  "search_for" : "NASPO2_SUPPLIER_CO",
  "data_type" : "JSON"
}

addCompany = {
  "event_id" : 71011,
  "first" : "Management",
  "last" : "Team",
  "company" : "Test Company, Inc.",
  "attendee_role_id" : "NASPO2_SUPPLIER_CO",
  "is_entity" : "Y",
  "attendee_type" : "E",
  "virtual" : "Y",
  "data_type" : "JSON"
}

attendeeList = {
  "event_id" : 71011,
  "search_fld" : "attendee_role_id",
  "search_for" : "NASPO2_STATE_REP",
  "data_type" : "JSON"
}




#print(events.all(auth, eventData))

#print(json.dumps(events.roles(auth, eventRoles),  indent=2))

#print(companies.add(auth, addCompany))

#print(json.dumps(companies.all(auth, addCompany), indent=2))

#print(attendees.add(auth, attendee_data))

#print(json.dumps(attendees.all(auth, attendeeList), indent=2))

#print(json.dumps(attendees.add(auth, company_data), indent=2))

#print(json.dumps(attendees.all(auth, attendeeList), indent=2))




company_data = {
  "event_id" : 70039,
  "first" : "Management",
  "last" : "Team",
  "company" : "Test Company, Inc.",
  "attendee_role_id" : "NASPO2_SUPPLIER_CO",
  "is_entity" : "Y",
  "attendee_type" : "E",
  "virtual" : "Y",
  "data_type" : "JSON"
}

#print(companies.add(auth, company_data))

company_rep = {
  "event_id" : 70039,
  'first' : 'Test', 
  'last' : 'SupplierRep2', 
  'company' : 'ABC, Inc.',
  'title' : 'Sales Rep',
  'attendee_role_id' : 'NASPO2_SUPPLIER_ATT',
  'email' : 'jhollinger@naspo.org',
  'username' : 'jhollinger@naspo.org',
  'password' : 'NASPO2021',
  'custom_12766' : 'This is my bio.',
  'custom_12784' : 'Eastern',
  'custom_7159' : 'https://naspo-events.s3.us-east-2.amazonaws.com/events/2021-exchange/photos/jonathanhollinger_101126409_jhollinger_photo_small.png',
  'custom_7581' : 'https://naspo-events.s3.us-east-2.amazonaws.com/events/2021-exchange/photos/jonathanhollinger_101126409_jhollinger_photo_small.png',
  'custom_7282' : 'https://naspo-events.s3.us-east-2.amazonaws.com/events/2021-exchange/photos/jonathanhollinger_101126409_jhollinger_photo_small.png',
  'custom_7664' : '2',
  'custom_9069' : 'Agricultural Equipment & Parks Equipment',
  'custom_8971' : 'No',
  'is_contact' : 'Y',
  'data_type' : 'JSON'
}

#print(attendees.add(auth, company_rep))




#print(attendees.edit(auth, edit_data))

edit_data = {
  "event_id" : 70039,
  "investor_id" : 3315088,
  'field_name' : 'attendee_role_id',
  'field_value' : 'NASPO2_OTHER_ATTENDEE',
  'data_type' : 'JSON',
}

print(attendees.edit(auth, edit_data))


supplier_att = [{
    'event_id': 70039,
    'first': 'Test',
    'last': 'Eastern Time',
    'company': 'Test Company, Inc.',
    'title': 'Test Supplier Title',
    'attendee_role_id': 'NASPO2_SUPPLIER_ATT',
    'email': 'test_supplier1@naspo.org',
    'username': 'test_supplier1@naspo.org',
    'password': 'exchange2021',
    'custom_12784': 'Eastern',
    'data_type': 'json'
},
{
    'event_id': 70039,
    'first': 'Test',
    'last': 'Central Time',
    'company': 'Test Company, Inc.',
    'title': 'Test Supplier Title',
    'attendee_role_id': 'NASPO2_SUPPLIER_ATT',
    'email': 'test_supplier2@naspo.org',
    'username': 'test_supplier2@naspo.org',
    'password': 'exchange2021',
    'custom_12784': 'Central',
    'data_type': 'json'
},
{
    'event_id': 70039,
    'first': 'Test',
    'last': 'Mountain Time',
    'company': 'Test Company, Inc.',
    'title': 'Test Supplier Title',
    'attendee_role_id': 'NASPO2_SUPPLIER_ATT',
    'email': 'test_supplier3@naspo.org',
    'username': 'test_supplier3@naspo.org',
    'password': 'exchange2021',
    'custom_12784': 'Mountain',
    'data_type': 'json'
},
{
    'event_id': 70039,
    'first': 'Test',
    'last': 'Pacific Time',
    'company': 'Test Company, Inc.',
    'title': 'Test Supplier Title',
    'attendee_role_id': 'NASPO2_SUPPLIER_ATT',
    'email': 'test_supplier4@naspo.org',
    'username': 'test_supplier4@naspo.org',
    'password': 'exchange2021',
    'custom_12784': 'Pacific',
    'data_type': 'json'
},
{
    'event_id': 70039,
    'first': 'Test',
    'last': 'Alaska Time',
    'company': 'Test Company, Inc.',
    'title': 'Test Supplier Title',
    'attendee_role_id': 'NASPO2_SUPPLIER_ATT',
    'email': 'test_supplier5@naspo.org',
    'username': 'test_supplier5@naspo.org',
    'password': 'exchange2021',
    'custom_12784': 'Alaska',
    'data_type': 'json'
},
{
    'event_id': 70039,
    'first': 'Test',
    'last': 'Hawaii Time',
    'company': 'Test Company, Inc.',
    'title': 'Test Supplier Title',
    'attendee_role_id': 'NASPO2_SUPPLIER_ATT',
    'email': 'test_supplier6@naspo.org',
    'username': 'test_supplier6@naspo.org',
    'password': 'exchange2021',
    'custom_12784': 'Hawaii',
    'data_type': 'json'
}
]


state_att = [{
    'event_id': 70039,
    'first': 'Test',
    'last': 'Eastern Time',
    'company': 'Test State',
    'title': 'Test Title',
    'attendee_role_id': 'NASPO2_STATE_REP',
    'email': 'test_state1@naspo.org',
    'username': 'test_state1@naspo.org',
    'password': 'exchange2021',
    'custom_12784': 'Eastern',
    'receive_request' : 'Y',
    'data_type': 'json'
},
{
    'event_id': 70039,
    'first': 'Test',
    'last': 'Central Time',
    'company': 'Test State',
    'title': 'Test Title',
    'attendee_role_id': 'NASPO2_STATE_REP',
    'email': 'test_supplier2@naspo.org',
    'username': 'test_state2@naspo.org',
    'password': 'exchange2021',
    'custom_12784': 'Central',
    'receive_request' : 'Y',
    'data_type': 'json'
},
{
    'event_id': 70039,
    'first': 'Test',
    'last': 'Mountain Time',
    'company': 'Test State',
    'title': 'Test Title',
    'attendee_role_id': 'NASPO2_STATE_REP',
    'email': 'test_state3@naspo.org',
    'username': 'test_state3@naspo.org',
    'password': 'exchange2021',
    'custom_12784': 'Mountain',
    'receive_request' : 'Y',
    'data_type': 'json'
},
{
    'event_id': 70039,
    'first': 'Test',
    'last': 'Pacific Time',
    'company': 'Test State',
    'title': 'Test Title',
    'attendee_role_id': 'NASPO2_STATE_REP',
    'email': 'test_state4@naspo.org',
    'username': 'test_state4@naspo.org',
    'password': 'exchange2021',
    'custom_12784': 'Pacific',
    'receive_request' : 'Y',
    'data_type': 'json'
},
{
    'event_id': 70039,
    'first': 'Test',
    'last': 'Alaska Time',
    'company': 'Test State',
    'title': 'Test Title',
    'attendee_role_id': 'NASPO2_STATE_REP',
    'email': 'test_state5@naspo.org',
    'username': 'test_state5@naspo.org',
    'password': 'exchange2021',
    'custom_12784': 'Alaska',
    'receive_request' : 'Y',
    'data_type': 'json'
},
{
    'event_id': 70039,
    'first': 'Test',
    'last': 'Hawaii Time',
    'company': 'Test State',
    'title': 'Test Title',
    'attendee_role_id': 'NASPO2_STATE_REP',
    'email': 'test_state6@naspo.org',
    'username': 'test_state6@naspo.org',
    'password': 'exchange2021',
    'custom_12784': 'Hawaii',
    'receive_request' : 'Y',
    'data_type': 'json'
}
]


#for x in state_att:
  #time.sleep(1)
  #print(attendees.add(auth, x))


