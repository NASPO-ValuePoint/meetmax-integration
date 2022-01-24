import os
import time
import json
import urllib
import requests
from requests_oauthlib import OAuth1Session
from meetmax import session
from meetmax import events
from meetmax import companies
from meetmax import attendees
from dotenv import load_dotenv
load_dotenv()

mm_key = os.getenv("MEETMAX_KEY")
mm_secret = os.getenv("MEETMAX_SECRET")
mm_test_id = 80471
auth = session.create(mm_key, mm_secret)

#Get Companies
all_companies = {
  "event_id" : mm_test_id,
  "search_fld" : "attendee_role_id",
  "search_for" : "NASPO2_SUPPLIER_CO",
  "data_type" : "json"
}

company_data = companies.all(auth, all_companies)

print(company_data)


# Test Data Objects
eventData = {
  "data_type" : "JSON"
}

eventRoles = {
  "event_id" : mm_test_id,
  "data_type" : "JSON"
}

companyData = {
  "event_id" : mm_test_id,
  "search_fld" : "attendee_role_id",
  "search_for" : "NASPO2_SUPPLIER_CO",
  "data_type" : "JSON"
}

addCompany = {
  "event_id" : mm_test_id,
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
  "event_id" : mm_test_id,
  "search_fld" : "attendee_role_id",
  "search_for" : "NASPO2_STATE_REP",
  "data_type" : "JSON"
}


company_data = {
  "event_id" : mm_test_id,
  "first" : "Management",
  "last" : "Team",
  "company" : "Test Company, Inc.",
  "attendee_role_id" : "NASPO2_SUPPLIER_CO",
  "is_entity" : "Y",
  "attendee_type" : "E",
  "virtual" : "Y",
  "data_type" : "JSON"
}

company_rep = {
  "event_id" : mm_test_id,
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

edit_data = {
  "event_id" : mm_test_id,
  "investor_id" : 3315088,
  'field_name' : 'attendee_role_id',
  'field_value' : 'NASPO2_OTHER_ATTENDEE',
  'data_type' : 'JSON',
}


supplier_att = [{
    'event_id': mm_test_id,
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
    'event_id': mm_test_id,
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
    'event_id': mm_test_id,
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
    'event_id': mm_test_id,
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
    'event_id': mm_test_id,
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
    'event_id': mm_test_id,
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
    'event_id': mm_test_id,
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
    'event_id': mm_test_id,
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
    'event_id': mm_test_id,
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
    'event_id': mm_test_id,
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
    'event_id': mm_test_id,
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
    'event_id': mm_test_id,
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

