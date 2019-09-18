#https://developers.google.com/sheets/api/reference/rest/v4/spreadsheets.values/get?apix_params=%7B%22spreadsheetId%22%3A%221HBAB-O1x6QtLcLfrQtWguIbW1MSd72vv94UsSOitN3c%22%2C%22range%22%3A%22A1%3AC3%22%7D
from pprint import pprint
import pickle
import os.path
from googleapiclient import discovery

creds = None #todo

if os.path.exists('token.pickle'):
    with open('token.pickle', 'rb') as token:
        creds = pickle.load(token)
# If there are no (valid) credentials available, let the user log in.
if not creds or not creds.valid:
    if creds and creds.expired and creds.refresh_token:
        creds.refresh(Request())
    else:
        flow = InstalledAppFlow.from_client_secrets_file(
            'credentials.json', SCOPES)
        creds = flow.run_local_server(port=0)
    # Save the credentials for the next run
    with open('token.pickle', 'wb') as token:
        pickle.dump(creds, token)

service = discovery.build('sheets', 'v4', credentials=creds)

# The ID of the spreadsheet to retrieve data from.
spreadsheet_id = '1HBAB-O1x6QtLcLfrQtWguIbW1MSd72vv94UsSOitN3c'  

# The A1 notation of the values to retrieve.
range_ = 'Sheet1!A1:C3'  

value_render_option = ''  

date_time_render_option = ''  # TODO: Update placeholder value.

request = service.spreadsheets().values().get(spreadsheetId=spreadsheet_id, range=range_)
response = request.execute()

# TODO: Change code below to process the `response` dict:
pprint(response['values'])

# response
# {
#   "range": "Sheet1!A1:C3",
#   "majorDimension": "ROWS",
#   "values": [
#     [
#       "日期",
#       "value",
#       "who"
#     ],
#     [
#       "9-18",
#       "12",
#       "Wade"
#     ],
#     [
#       "9-19",
#       "23",
#       "Deng"
#     ]
#   ]
# }

# upsert to mysql