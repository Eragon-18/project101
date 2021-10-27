import dropbox

class TransferData:
    def __init__(self, accessToken):
        self.accessToken = accessToken

    def uploadFiles(self, source, destination):
        dbx = dropbox.Dropbox(self.accessToken)

        f = open(source, "rb")
        dbx.files_upload(f.read(),destination, mode = WriteMode('overwrite'))

def main():
    accessToken = "qPFQRDjytw8AAAAAAAAAAdJnIQXryPMadg3y-Ux9LYl-CKTZsZKDpHYoc4Ap_Dj_"
    uF = TransferData(accessToken)

    source = input("Enter file path")
    destination = input("Enter location on dropbox")

    uF.uploadFiles(source,destination)
    print("File has been uploaded.")

if __name__ == "__main__":
    main()