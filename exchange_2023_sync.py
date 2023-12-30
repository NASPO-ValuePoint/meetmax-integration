import os
import psycopg2.extras
#import oauthlib
#from requests_oauthlib import OAuth1Session
from meetmax import session
from meetmax import events
from meetmax import companies
from meetmax import attendees
from meetmax import helpers
import warehouse
from dotenv import load_dotenv
load_dotenv()

mm_key = os.getenv("mm_key")
mm_secret = os.getenv("mm_secret")

# Connect to meetmax api
try:
    auth = session.create(mm_key, mm_secret)
    #print(auth)
except Exception as e:
    print(e)

#Connect to data warehouse
try:
    conn = psycopg2.connect(host=os.environ.get("DB_HOST"), database=os.environ.get(
        "DB_DATABASE"), user=os.environ.get("DB_USER"), password=os.environ.get("DB_PASSWORD"))
except Exception as e:
    print(e)

def standaradize_company_names():
    #Check if Clean_Company_exchange.sql has been run
    query = '''
    with company_names as 
    (
        select distinct "Company" as name
        from warehouse.pbi_registrations_all_events
        where "EventID" = '61725C13-6C78-41C9-A947-44BCE8ABE2CB'
            and "Status" <> 'Cancelled'
            and "Company" <> ''
    )
    INSERT INTO warehouse.cvent_organizations(original_name, standardized_name, needs_review)
    select company_names.name, company_names.name, True from company_names
    left join warehouse.cvent_organizations o on company_names.name = o.original_name
    where o.id is null
    RETURNING *;
    '''
    data = warehouse.get_query_data(conn, query)
    #print(data)
    if len(data) > 0:
        print('Adding new company names to warehouse.cvent_organizations')
        for d in data:
            print(f'New Company - {d["original_name"]}')
        print('Review the new companies before running the next steps')
        exit()

    #Check if all standardized company names have been reviewed
    query = '''select * from warehouse.cvent_organizations
                where needs_review = true;
                '''
    result = warehouse.get_query_data(conn, query)
    if len(result) > 0:
        print(f'''{len(result)} companies have not been reviewed.\nPlease review the standardized names and set needs_review to False before moving to the next step''')
        exit()
    return

def sync_company_names(event_id):
    company_mm = companies.all(auth, event_id)
    # Get the name of the company from the results
    company_map = map(lambda x: x['company'], company_mm['results'])
    company_list = list(company_map)
    #print(company_list)
    query_companies = '''SELECT DISTINCT "Company" 
                            FROM warehouse.exchange_meetmax_2023 
                            WHERE attendee_role_id = 'NASPO2_SUPPLIER_ATT';
                         '''
    companies_db = warehouse.get_query_data(conn, query_companies)
    #print(companies_db)
    for c in companies_db:
        # print(c['Company'])
        if c['Company'] in company_list:
            print(f"Already in meetmax - {c['Company']}")
        else:
            print(f'To be added - {c["Company"]}')
            added = companies.add(auth, c, event_id)
            #print(added)
            if 'status_code' not in added:
                print(f'Unable to add {c["Company"]}. Error: {added["error"]}')
                print('Please check the error and try again before adding suppliers')
                exit()
    return

#Get "Making 1-on-1 appointments/Suppliers bucket" information from warehouse
def sync_suppliers(event_id):
    query_attendee = '''SELECT * FROM warehouse.exchange_meetmax_2023 
                        WHERE meetmax_id is NULL 
                        AND meetmax_status is NULL 
                        AND "One-on-One appointments" = 'Yes' 
                        AND attendee_role_id = 'NASPO2_SUPPLIER_ATT'
                        '''
    data = warehouse.get_query_data(conn, query_attendee)
    print('Total NASPO2_SUPPLIER_ATT to add - ', len(data))
    # add their info to meetmax
    for a in data:
        # print(a)
        attendee_status = attendees.add_supplier(auth, a, event_id)
        #print(attendee_status)
        warehouse.insert_meetmax_status(conn, a, attendee_status)
    return

#Get "Taking 1-on-1 appointments/State Members bucket" information from warehouse
def sync_state_members(event_id):
    query_attendee = '''SELECT * FROM warehouse.exchange_meetmax_2023 
                        WHERE meetmax_id is NULL 
                        AND meetmax_status is NULL
                        AND "One-on-One appointments" = 'Yes' 
                        AND attendee_role_id in ('NASPO2_STATE_REP', 'NASPO2_NASPO_REP');
                            '''
    data = warehouse.get_query_data(conn, query_attendee)
    print('Total NASPO2_STATE_REP to add - ', len(data))
    # add their info to meetmax
    for a in data:
        # print(a)
        attendee_status = attendees.add_statemember(auth, a, event_id)
        # print(attendee_status)
        warehouse.insert_meetmax_status(conn, a, attendee_status)
    return

#Other attendees not participating in one-on-one appointments
def sync_others(event_id):
    query_attendee = '''SELECT * FROM warehouse.exchange_meetmax_2023 
                        WHERE coalesce("One-on-One appointments", 'No') = 'No' 
                        AND meetmax_id is NULL 
                        AND meetmax_status is NULL;
                     '''
    data = warehouse.get_query_data(conn, query_attendee)
    print('Total NASPO2_OTHER_ATTENDEE to add - ', len(data))
    # add their info to meetmax
    for a in data:
        # print(a)
        attendee_status = attendees.add_other(auth, a, event_id)
        # print(attendee_status)
        warehouse.insert_meetmax_status(conn, a, attendee_status)
    return


mm_test_id = 90203
mm_id = 90199
standaradize_company_names()
# sync_company_names(mm_id)
# sync_suppliers(mm_id)
# sync_state_members(mm_id)
# sync_others(mm_id)