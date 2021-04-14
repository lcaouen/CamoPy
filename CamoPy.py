import logging
import time
import json
from time import sleep
from camera import Camera
from onedrive import OneDrive
from mail import Mail
from taskWeb import TaskWeb

def main(args):
    logging.basicConfig(format='%(asctime)-15s - %(levelname)s:%(message)s', filename='camopy.log', level=logging.DEBUG)
    with open('./config.json', 'r') as fichier:
        config = json.load(fichier)

    mythread = TaskWeb(config)
    mythread.start()

    mail = Mail(config)
    path = config["images"]["path"]
    onedrive = OneDrive(config)
    itemImages = onedrive.getItem("root", "Images")
    itemCamopy = onedrive.getItem(itemImages.id, config["oneDrive"]["directory"])

    if itemCamopy == None:
        itemCamopy = onedrive.createFolder(itemImages.id, config["oneDrive"]["directory"])

    sendMail = True
    camera = Camera(config)
    run = True
    while run :
        start = time.clock()
        fileName = camera.capture(path)
        end = time.clock()
        #logging.debug("Motion detection : {}".format(end - start))

        if (fileName != ""):
            start = time.clock()
            onedrive.upload(itemCamopy.id, path, fileName)
            end = time.clock()
            logging.info("Uploaded file {} : {}".format(fileName, end - start))
            if sendMail:
                #message = "\n".join(config["mail"]["message"])
                #mail.connect()
                #mail.sendMessage(message)
                #mail.disConnect()
                sendMail = False
                lastMail = time.clock()
                logging.info("email sent")
            else:
                if time.clock() - lastMail > config["mail"]["wait"] :
                    sendMail = True

    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
