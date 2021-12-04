import dropbox
import os

class TransferData:
    def __init__(self, access_token):
        self.access_token = access_token

    def upload_file(self, file_from, file_to):
        dbx = dropbox.Dropbox(self.access_token)

        for root, dirs, files in os.walk(file_from):
            relative_path = os.paths.relpath(local_path, file_from)
            dropbox_path = os.path.join(file_to, relative_path)
            for filename in files: 
                local_path = os.path.join(root, filename)
            with open(file_from, 'rb') as f:
                dbx.files_upload(f.read(), dropbox_path, mode=WriteMode('overwrite'))
        

def main():
    access_token = 'ScCnNIeInuUAAAAAAAAAAShZGoNpDyRkSfkOGJx7UaG_SeLI4Uq4KmPoVCqoRrJQ'
    transferData = TransferData(access_token)

    file_from = input("Enter your source file : ")
    file_to = input("Enter your file destination : ")

    # API v2
    transferData.upload_file(file_from, file_to)
    print("File has been uploaded.")

main()