from pydrive.drive import GoogleDrive
from pydrive.auth import GoogleAuth

g_auth = GoogleAuth()
g_auth.LocalWebserverAuth()

drive = GoogleDrive(g_auth)


# View all folders and file in your Google Drive
fileList = drive.ListFile(
    {'q': "'root' in parents and trashed=false"}).GetList()

for file in fileList:
    print('Title: %s, ID: %s' % (file['title'], file['id']))
    # Get the folder ID that you want
    if(file['title'] == "To Share"):
        fileID = file['id']
