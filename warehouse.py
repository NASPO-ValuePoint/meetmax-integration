import os
import json
import psycopg2
from dotenv import load_dotenv
load_dotenv()

def get_query_data(conn, query):
    cur = conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor)
    cur.execute(query)
    data = cur.fetchall()
    conn.commit()
    cur.close()
    return data

def insert_meetmax_status(conn, cvent_record, meetmax_status):
    cur = conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor)
    if "status_code" in meetmax_status:
        cur.execute('''INSERT INTO warehouse.cvent_meetmax(registration_id, meetmax_id)
                            VALUES(%s, %s)''',
                    (cvent_record["Registration ID"], meetmax_status['id'])
                    )
        print(cvent_record["Registration ID"] + " - Attendee Added.")
    else:
        cur.execute('''INSERT INTO warehouse.cvent_meetmax(registration_id, meetmax_status)
                            VALUES(%s, %s)''', (cvent_record["Registration ID"], str(meetmax_status))
                    )
        print(cvent_record["Registration ID"] + " - Error Adding Attendee.")
    conn.commit()
    cur.close()
    return
