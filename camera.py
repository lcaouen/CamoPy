import logging
import datetime
import os
from time import sleep
from picamera import PiCamera
from io import BytesIO
from PIL import Image, ImageChops, ImageDraw, ImageFilter


class Camera:

    def __init__(self, config):
        self.image = None
        self.imagePrev = None
        self.imageDiff = None

        self.camera = PiCamera(resolution=(config["images"]["width"], config["images"]["height"]), framerate=config["images"]["framerate"])
        # Set ISO to the desired value
        self.camera.iso = config["images"]["iso"]
        # Wait for the automatic gain control to settle
        sleep(2)
        # Now fix the values
        self.camera.shutter_speed = config["images"]["shutter_speed"]
        self.camera.exposure_mode = config["images"]["exposure_mode"]
        self.camera.brightness = config["images"]["brightness"]
        self.camera.contrast = config["images"]["contrast"]

        self.threshold = config["images"]["threshold"]
        self.detection = config["images"]["detection"]
        self.width = config["images"]["width"]
        self.height = config["images"]["height"]

    def capture(self, path):
        fileName = ""
        stream = BytesIO()
        self.camera.capture(stream, format='jpeg')
        # "Rewind" the stream to the beginning so we can read its content
        stream.seek(0)
        self.image = Image.open(stream)
        if self.imagePrev is not None and self.detection :
            self.imageDiff = ImageChops.difference(self.image, self.imagePrev)
            # self.imageDiff.filter(ImageFilter.BLUR)
            self.imageDiff = self.imageDiff.point(lambda i: i > self.threshold and 255)
            box = self.imageDiff.getbbox()
            histo = self.imageDiff.convert('L').histogram()
            nPixels = self.width * self.height - histo[0]
            if box is not None and nPixels > 10 :
                draw = ImageDraw.Draw(self.imageDiff)
                draw.rectangle(box, outline='white')

                directory = datetime.date.today().isoformat()
                if not os.path.exists(path + directory):
                    os.makedirs(path + directory)

                fileName = datetime.datetime.today().isoformat().replace(":", "-")
                self.image.save(path + directory + '/' + fileName + '-img.jpg')
                self.imageDiff.save(path + directory + '/' + fileName + '-diff.jpg')
                fileName = directory + '/' + fileName + '-img.jpg'
        self.imagePrev = self.image
        return fileName
