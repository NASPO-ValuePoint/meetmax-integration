import requests


# Get Events
def all(session, data):
    url = 'https://meetmax.com/sched/service/event/list'
    try:
        r = session.get(url, params=data)
        r.raise_for_status()
        return r.json()

    except requests.exceptions.HTTPError as e:
        return e.response.json()


# Get Event Roles
def roles(session, data):
    url = 'https://meetmax.com/sched/service/attendeerole/list'
    try:
        r = session.get(url, params=data)
        r.raise_for_status()
        return r.json()

    except requests.exceptions.HTTPError as e:
        return e.response.json()
