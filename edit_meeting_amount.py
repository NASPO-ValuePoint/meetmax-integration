import os
import time

import psycopg2.extras
from dotenv import load_dotenv

from meetmax import attendees
from meetmax import session

load_dotenv()

mm_key = os.getenv("MEETMAX_KEY")
mm_secret = os.getenv("MEETMAX_SECRET")
mm_event_id = 70039

auth = session.create(mm_key, mm_secret)

conn = psycopg2.connect(host=os.environ.get("DB_HOST"), database=os.environ.get(
    "DB_DATABASE"), user=os.environ.get("DB_USER"), password=os.environ.get("DB_PASSWORD"))
cur = conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor)

# Get Registrations
registrations = "SELECT * FROM conferences_events.exchange_meetmax WHERE meetmax_id IS NOT NULL and meetings = 0;"
cur.execute(registrations)
res = cur.fetchall()
for x in res:
    # Wait for One Sec Between Records
    time.sleep(1)
    edit_data = {
        "event_id": mm_event_id,
        "investor_id": x["meetmax_id"],
        'field_name': 'custom_7664',
        'field_value': x["meetings"],
        'data_type': 'JSON',
    }

    print(attendees.edit(auth, edit_data))

    conn.commit()

cur.close()
conn.close()
