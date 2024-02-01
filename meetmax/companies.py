import time

import requests


# Get Companies - Data requires search_fld, and search_for. https://www.meetmax.com/docs/service/company_list.html
def all(session, event_id):
    url = 'https://meetmax.com/sched/service/attendee/list'
    all_companies = {
        "event_id": event_id,
        "search_fld": "attendee_role_id",
        "search_for": "NASPO3_SUPPLIER_CO",
        "data_type": "json"
    }
    try:
        r = session.get(url, params=all_companies)
        time.sleep(5)
        r.raise_for_status()
        return r.json()

    except requests.exceptions.HTTPError as e:
        return e.response.json()


# Add Company - Data requires event_id, first, last, company, attendee_role_id, is_entity, attendee_type, virtual. https://www.meetmax.com/docs/service/company_add.html
def add(session, record, event_id):
    url = 'https://meetmax.com/sched/service/attendee/add'
    company_data = {
        "event_id": event_id,
        "first": "Management",
        "last": "Team",
        "company": record['Company'],
        "attendee_role_id": "NASPO3_SUPPLIER_CO",
        "is_entity": "Y",
        "attendee_type": "E",
        "virtual": "Y",
        "data_type": "JSON"
    }
    time.sleep(4)
    try:
        r = session.get(url, params=company_data)
        r.raise_for_status()
        return r.json()

    except requests.exceptions.HTTPError as e:
        return e.response.json()
