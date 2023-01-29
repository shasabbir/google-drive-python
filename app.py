from oauth2client.service_account import ServiceAccountCredentials
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload

SERVICE_ACCOUNT = 'glpyy-376212-6ef6f03254b0.json' # Please set the file of your credentials of service account.
UPLOAD_FILE = 'a.txt' # Please set the filename with the path you want to upload.
FOLDER_ID = '1BQY5YyGjRvG-FMP3PrEILu8NfD-JWXud' # Please set the folder ID that you shared your folder with the service account.
FILENAME = 'a.txt' # You can set the filename of the uploaded file on Google Drive.

SCOPES = ['https://www.googleapis.com/auth/drive']
credentials = ServiceAccountCredentials.from_json_keyfile_name(SERVICE_ACCOUNT, SCOPES)
drive = build('drive', 'v3', credentials=credentials)
metadata = {'name': FILENAME, "parents": [FOLDER_ID]}
file = MediaFileUpload(UPLOAD_FILE, resumable=True)
response = drive.files().create(body=metadata, media_body=file).execute()
fileId = response.get('id')
print(fileId)  # You can see the file ID of the uploaded file.
