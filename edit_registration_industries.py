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
registrations = '''SELECT * FROM conferences_events.exchange_meetmax WHERE registration_id IN (
'783661991',
'783660218',
'783653863',
'783552403',
'780265642',
'782956067',
'782566833',
'781849508',
'780973140',
'780961650',
'780257208',
'779844374',
'779830388',
'778682919',
'777581331',
'783544068',
'783427241',
'781739638')'''

cur.execute(registrations)
res = cur.fetchall()
for x in res:
    # Wait for One Sec Between Records
    time.sleep(1)
    edit_data = {
        "event_id": 70039,
        "investor_id": x["meetmax_id"],
        'field_name': 'custom_9069',
        'field_value': x["industries"],
        'data_type': 'JSON',
    }

    print(attendees.edit(auth, edit_data))

cur.close()
conn.close()
