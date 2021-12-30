import os
import meetmax
from dotenv import load_dotenv
load_dotenv()

mm_key = os.getenv("MEETMAX_KEY")
mm_secret = os.getenv("MEETMAX_SECRET")
mm_event = 71011

#OAuth1 Sign Request
auth = meetmax.signature(mm_key, mm_secret)

#Add NVP Representative Attendee - This requests is successful selecting options 1, 2, 3, 4, 5, 6, 7, 8, 9.
attendee_data_1 = {
    'event_id': mm_event,
    'crm_id': '728128242',
    'first': 'Voight',
    'last': 'Shealy',
    'company': 'NASPO ValuePoint',
    'title': 'Cooperative Contract Coordinator III',
    'telephone': '(803) 760-0302',
    'attendee_role_id': 'NASPO2_NASPO_REP',
    'email': 'test_vshealy@naspovaluepoint.org',
    'username': 'test_vshealy@naspovaluepoint.org',
    'password': 'exchange2021',
    'custom_12766': 'Voight Shealy is a Cooperative Contract Coordinator III for NASPO ValuePoint with the primary responsibilities for education and outreach activities, including conferences, trade shows, member visits, and facilitation of contract adoption by state and local government agencies. ',
    'custom_12784': 'Eastern',
    'receive_request': 'Y',
    'custom_7581': 'https://naspo-events.s3.us-east-2.amazonaws.com/events/2021-exchange/photos/voightshealy_101126409_shealy3.jpg',
    'custom_9069': [1,2,3,4,5,6,7,8,9],
    'data_type': 'json'
}

attendee = meetmax.add_attendee(auth, attendee_data_1)
print("Adding attendee 1.")
print(attendee)



#Add NVP Representative Attendee - This requests is not successful selecting options 1, 2, 3, 4, 5, 6, 7, 8, 9, 10
attendee_data_2 = {
    'event_id': mm_event,
    'crm_id': '728128242',
    'first': 'Voight',
    'last': 'Shealy',
    'company': 'NASPO ValuePoint',
    'title': 'Cooperative Contract Coordinator III',
    'telephone': '(803) 760-0302',
    'attendee_role_id': 'NASPO2_NASPO_REP',
    'email': 'test_vshealy@naspovaluepoint.org',
    'username': 'test_vshealy@naspovaluepoint.org',
    'password': 'exchange2021',
    'custom_12766': 'Voight Shealy is a Cooperative Contract Coordinator III for NASPO ValuePoint with the primary responsibilities for education and outreach activities, including conferences, trade shows, member visits, and facilitation of contract adoption by state and local government agencies. ',
    'custom_12784': 'Eastern',
    'receive_request': 'Y',
    'custom_7581': 'https://naspo-events.s3.us-east-2.amazonaws.com/events/2021-exchange/photos/voightshealy_101126409_shealy3.jpg',
    'custom_9069': [1,2,3,4,5,6,7,8,10],
    'data_type': 'json'
}


attendee = meetmax.add_attendee(auth, attendee_data_2)
print("Adding attendee 2.")
print(attendee)