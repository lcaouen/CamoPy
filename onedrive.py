import logging
import onedrivesdk
from os import listdir
from os.path import isfile, join

class OneDrive:

    def __init__(self, config):
        redirect_uri = "http://" + config["webService"]["name"] + ":" + str(config["webService"]["port"])
        client_secret = config["oneDrive"]["clientSecret"]
        client_id = config["oneDrive"]["clientId"]
        api_base_url = config["oneDrive"]["url"]
        scopes = ['wl.signin', 'wl.offline_access', 'onedrive.readwrite']

        http_provider = onedrivesdk.HttpProvider()
        auth_provider = onedrivesdk.AuthProvider(
            http_provider=http_provider,
            client_id=client_id,
            scopes=scopes)

        loaded = True
        #reload session ??
        try:
            auth_provider.load_session()
            auth_provider.refresh_token()
        except:
            loaded = False
        #reload session ??


        self.client = onedrivesdk.OneDriveClient(api_base_url, auth_provider, http_provider)
        if loaded == False :
            auth_url = self.client.auth_provider.get_auth_url(redirect_uri)
            # Ask for the code
            print('Paste this URL into your browser, approve the app\'s access.')
            print('Copy everything in the address bar after "code=", and paste it below.')
            print(auth_url)
            code = input('Paste code here: ')

            self.client.auth_provider.authenticate(code, redirect_uri, client_secret)

        auth_provider.save_session()

    def getItem(self, parentID, name):
        items = self.client.item(id=parentID).children.get()
        for item in items:
            if item.name == name:
                return item
        return None

    def createFolder(self, parentID, name):
        f = onedrivesdk.Folder()
        i = onedrivesdk.Item()
        i.name = name
        i.folder = f
        return self.client.item(drive='me', id=parentID).children.add(i)

    def upload(self, id, path, fileName):
        try:
            paths = fileName.split("/")
            if len(paths) == 2:
                directory = self.createFolder(id, paths[0])
                self.client.item(drive='me', id=directory.id).children[paths[1]].upload(join(path, fileName))
        except:
            logging.error("Error when uploading file " + fileName)
