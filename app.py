from oauth2client.service_account import ServiceAccountCredentials
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload
import io
from googleapiclient.http import MediaIoBaseDownload
import json
SERVICE_ACCOUNT = 'glpyy-376212-6ef6f03254b0.json' # Please set the file of your credentials of service account.
UPLOAD_FILE = 'b.txt' # Please set the filename with the path you want to upload.
FOLDER_ID = '1BQY5YyGjRvG-FMP3PrEILu8NfD-JWXud' # Please set the folder ID that you shared your folder with the service account.
FILENAME = 'b.txt' # You can set the filename of the uploaded file on Google Drive.

SCOPES = ['https://www.googleapis.com/auth/drive']
credentials = ServiceAccountCredentials.from_json_keyfile_name(SERVICE_ACCOUNT, SCOPES)
drive = build('drive', 'v3', credentials=credentials)


def create_file(name,folder_id,filedir):
    metadata = {'name': name, "parents": [folder_id]}
    file = MediaFileUpload(filedir, resumable=True)

    response = drive.files().create(body=metadata, media_body=file).execute()
    fileId = response.get('id')
    print(fileId)  # You can see the file ID of the uploaded file.
    return fileId
def delete_file(file_id):
    try:
        drive.files().delete(fileId=file_id).execute()
        return True
    except:
        return False

def download_file(name,file_id):
    request = drive.files().get_media(fileId=file_id)
    fh = io.FileIO(name, 'wb')
    downloader = MediaIoBaseDownload(fh, request)
    done = False
    while done is False:
        status, done = downloader.next_chunk()
        print ("Download  done")
        f = open(name, "r")
        return (json.loads(f.read()))
#print(download_file('nn.txt','1K0g6A4VvqlKahRmm00MDiKk-fDVDK3U6')['text'])
create_file("gg.txt",FOLDER_ID,"gg.txt")
#print(delete_file("1K0g6A4VvqlKahRmm00MDiKk-fDVDK3U6"))