import dropbox

class UploadData:
    def __init__(self, accesstoken):
        self.accesstoken = accesstoken
    def UploadFiles(self, source, destination):
        dbx = dropbox.Dropbox(self.accesstoken)
        file = open(source, "rb")
        dbx.files_upload(file.read(), destination)

def main():
    accesstoken = "VHMEONWemcQAAAAAAAAAAQ4xES4pPN-OQHZnFEXLPYMD8RuLBTR456Mk0Kne4gsN"
    transferData = UploadData(accesstoken)
    source = "C:/Users/Raghav/Desktop/Madhav/New folder (9)/madhav/Python1/py/File1.py"
    destination = "/test/New.py"
    transferData.UploadFiles(source, destination)
    print("File Has Been Moved")
    
main()
